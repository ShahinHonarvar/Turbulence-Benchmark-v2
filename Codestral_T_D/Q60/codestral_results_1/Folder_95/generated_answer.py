def all_left_right_truncatable_prime(t):

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
    x = t[77]
    trunc_primes = [p for p in range(2, x + 1) if is_prime(p) and '0' not in str(p)]
    lr_trunc_primes = []
    for p in trunc_primes:
        tl = truncate_left(p)
        tr = truncate_right(p)
        while tl > 0 and tr > 0:
            if not is_prime(tl) or not is_prime(tr):
                break
            tl = truncate_left(tl)
            tr = truncate_right(tr)
        else:
            lr_trunc_primes.append(p)
    return sorted(lr_trunc_primes)