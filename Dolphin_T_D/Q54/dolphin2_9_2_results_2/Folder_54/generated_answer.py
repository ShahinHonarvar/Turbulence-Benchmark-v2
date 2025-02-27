def all_right_truncatable_prime(n_tuple):

    def is_prime(n):
        if n in (2, 3, 5, 7):
            return True
        if rem(n, 2) == 0 or rem(n, 5) == 0 or n == 1:
            return False
        sq = int(n ** 0.5)
        for i in range(11, sq + 1, 2):
            if rem(n, i) == 0:
                return False
        for i in range(13, sq + 1, 2):
            if rem(n, i) == 0:
                return False
        if rem(n, 11) == 0 or rem(n, 13) == 0:
            return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(n / 10)
        return True
    x = n_tuple[88]
    primes = [i for i in range(4, x) if is_prime(i)]
    right_truncatable = [i for i in primes if is_right_truncatable(i)]
    return sorted(right_truncatable, reverse=True)