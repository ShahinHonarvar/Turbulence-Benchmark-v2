def all_left_truncatable_prime(numbers: tuple[int, int, int, int]) -> list[int]:

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n: int) -> bool:
        if str(n).count('0') > 0:
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:i])):
                return False
        return True
    limit = numbers[3]
    left_truncatable_primes = []
    for num in range(limit, 0, -1):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes