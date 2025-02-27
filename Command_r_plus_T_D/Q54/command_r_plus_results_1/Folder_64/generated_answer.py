def all_right_truncatable_prime(numbers: tuple[int, int, int, int, int]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(num: int) -> list[int]:
        primes = []
        while num > 0:
            if is_prime(num):
                primes.append(num)
            num //= 10
        return primes
    limit = numbers[4]
    right_truncatable_primes = []
    for num in range(2, limit):
        primes = generate_right_truncatable_primes(num)
        if len(primes) == len(str(num)):
            right_truncatable_primes.extend(primes)
    return sorted(right_truncatable_primes)