def all_left_right_truncatable_prime(tup):
    x = tup[84]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])

    def is_left_truncatable(n):
        while n >= 10:
            n = truncate_left(n)
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        while n >= 10:
            n = truncate_right(n)
            if not is_prime(n):
                return False
        return True
    truncatable_primes = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        if is_prime(n) and is_left_truncatable(n) and is_right_truncatable(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)