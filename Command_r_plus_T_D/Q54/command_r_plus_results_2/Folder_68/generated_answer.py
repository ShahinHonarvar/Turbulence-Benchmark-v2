def all_right_truncatable_prime(numbers: tuple[int, int]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num: int) -> bool:
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    primes = []
    for i in range(numbers[1]):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)