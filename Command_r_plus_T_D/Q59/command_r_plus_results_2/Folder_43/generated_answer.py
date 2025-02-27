def all_left_truncatable_prime(limit: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def left_truncatable_prime(num: int) -> bool:
        if str(num).count('0') > 0:
            return False
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[:i])):
                return False
        return is_prime(num)
    left_truncatable_primes = []
    for i in range(2, limit[89]):
        if left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)