def all_left_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        m = int(n ** 0.5) + 1
        for x in range(3, m, 2):
            if n % x == 0:
                return False
        return True
    x = x_tuple[88]
    trunc_primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            s = str(i)
            if not '0' in s and len(s) > 1:
                s_trunc = s[1:-1]
                while s_trunc and is_prime(int(s_trunc)):
                    if len(s_trunc) == 1 or is_prime(int(s_trunc[1:-1])):
                        trunc_primes.append(int(s))
                    s_trunc = s_trunc[1:-1]
    return sorted(trunc_primes, reverse=True)