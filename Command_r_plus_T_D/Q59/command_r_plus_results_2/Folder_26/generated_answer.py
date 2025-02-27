def all_left_truncatable_prime(limit: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def left_truncate(num: int) -> list[int]:
        str_num = str(num)
        left_truncatable = [int(str_num[:i]) for i in range(1, len(str_num))]
        left_truncatable.append(num)
        return left_truncatable
    left_truncatable_primes = []
    for num in range(2, limit[81]):
        if str(num).count('0') > 0:
            continue
        if all((is_prime(n) for n in left_truncate(num))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)