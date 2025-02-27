def all_left_right_truncatable_prime(x: tuple[int]) -> list[int]:
    """
    All left-right-truncatable prime numbers in [1, x].
    """
    nums = filter(lambda n: '0' not in str(n), range(2, x + 1))

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = filter(is_prime, nums)
    truncatable_primes = []
    for p in primes:
        str_p = str(p)
        for i in range(1, len(str_p)):
            if not (is_prime(int(str_p[:i])) and is_prime(int(str_p[i:]))):
                break
        else:
            truncatable_primes.append(p)
    return sorted(truncatable_primes)