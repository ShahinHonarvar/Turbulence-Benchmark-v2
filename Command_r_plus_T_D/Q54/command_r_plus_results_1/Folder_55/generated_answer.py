def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncate(num: int) -> list[int]:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        return digits[::-1]
    limit = numbers[73]
    right_truncatable_primes = []
    for num in range(2, limit):
        if is_prime(num):
            digits = right_truncate(num)
            is_truncatable = all((is_prime(int(''.join(digits[:i]))) for i in range(1, len(digits) + 1)))
            if is_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)