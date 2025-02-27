def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(limit: int) -> list[int]:
        primes = []
        for num in range(limit, 0, -1):
            if is_prime(num) and all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num))))):
                primes.append(num)
        return primes
    x = numbers[93]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    return sorted(right_truncatable_primes)