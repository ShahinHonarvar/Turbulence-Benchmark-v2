def all_left_right_truncatable_prime(y):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable_prime(n, primes):
        if n < 10:
            return True
        if n not in primes[n // 10]:
            return False
        m, c, d = (n, 10, 1)
        while n >= 10:
            c *= 10
            d *= 10
            n //= 10
            if n not in primes[n]:
                return False
        return is_truncatable_prime(n, primes)
    primes = {2: set([2])}
    p = 3
    while p <= y:
        if is_prime(p):
            s = {p}
            while p <= y:
                p *= 10
                s.add(p)
                primes[p] = s
        p += 2
    l = []
    for p in primes:
        if is_truncatable_prime(p, primes):
            l.append(p)
    l.sort()
    return l