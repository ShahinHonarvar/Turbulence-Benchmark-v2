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
        for i in range(10 ** len(str(num)), num + 1):
            if is_prime(i) and all((is_prime(int(str(i)[:j])) for j in range(1, len(str(i))))):
                primes.add(i)
        return primes
    right_truncatable_primes = generate_right_truncatable_primes(numbers[100])
    return sorted(list(right_truncatable_primes))