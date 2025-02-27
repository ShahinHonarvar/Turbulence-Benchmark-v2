def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(num: int) -> list[int]:
        primes = []
        for i in range(10):
            if is_prime(num):
                primes.append(num)
            num //= 10
        return primes
    x = numbers[992]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            right_truncatable_primes.extend(generate_right_truncatable_primes(num))
    return sorted(set(right_truncatable_primes))