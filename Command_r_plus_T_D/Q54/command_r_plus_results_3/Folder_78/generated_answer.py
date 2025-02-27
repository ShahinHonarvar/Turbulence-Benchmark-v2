def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(n: int) -> list[int]:
        primes = []
        for i in range(10 ** n):
            num = i
            is_prime_num = True
            for _ in range(n):
                if not is_prime(num):
                    is_prime_num = False
                    break
                num //= 10
            if is_prime_num:
                primes.append(i)
        return primes
    limit = numbers[23]
    return sorted(generate_right_truncatable_primes(len(str(limit))))