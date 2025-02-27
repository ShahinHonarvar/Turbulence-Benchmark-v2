from math import ceil, sqrt
    from itertools import count

def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if not n % 2 or n <= 1:
            return False
        for p in count(3, 2):
            if p > sqrt(n):
                break
            if not n % p:
                return False
        return True

    def gen_primes():
        for n in count(2):
            if is_prime(n):
                yield n

    def digits(n):
        yield from reversed([int(d) for d in str(n)])

    def left_truncatable(p):
        if not all((0 < d < 10 for d in digits(p))):
            return False
        d = 10 ** (len(str(p)) - 1)
        for i in count(1):
            dp = digits(p // d)
            if not is_prime(p):
                return False
            if not all((is_prime(d) for d in dp)):
                return False
            if d == 1:
                return True
            p %= d
            d //= 10
    p = t[618]
    s = [i for i in gen_primes() if i < p and left_truncatable(i)]
    return sorted(s)