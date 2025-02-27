def all_left_truncatable_prime(limit_tup: tuple[int]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def left_truncatable(num: int) -> bool:
        if num < 10 or str(num).count('0') > 0:
            return False
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[:i])):
                return False
        return True
    limit = limit_tup[87]
    left_truncatable_primes = []
    for num in range(2, limit):
        if left_truncatable(num) and is_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)