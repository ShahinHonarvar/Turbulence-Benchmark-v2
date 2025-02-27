def all_left_truncatable_prime(numbers: tuple[int, int, int, int]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_left_truncatable_primes(limit: int) -> list[int]:
        primes = []
        for num in range(limit, 0, -1):
            if str(num).count('0') > 0:
                continue
            while num > 0 and is_prime(num):
                primes.append(num)
                num = int(str(num)[:-1]) if len(str(num)) > 1 else 0
        return primes
    limit = numbers[3]
    left_truncatable_primes = generate_left_truncatable_primes(limit)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes