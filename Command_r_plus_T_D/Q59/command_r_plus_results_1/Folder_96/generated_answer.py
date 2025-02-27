def all_left_truncatable_prime(limit_tup: tuple[int]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    limit = limit_tup[29]
    left_truncatable_primes = []
    for i in range(2, limit):
        if str(i).count('0') > 0:
            continue
        temp = i
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)