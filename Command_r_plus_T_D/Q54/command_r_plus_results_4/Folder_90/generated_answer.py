def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(num: int) -> set[int]:
        primes = set()
        for i in range(10 ** len(str(num)) - 1, 0, -1):
            if is_prime(i) and is_prime(i // 10):
                primes.add(i)
        return primes
    limit = numbers[466]
    right_truncatable_primes = generate_right_truncatable_primes(limit)
    return sorted(list(right_truncatable_primes), reverse=True)