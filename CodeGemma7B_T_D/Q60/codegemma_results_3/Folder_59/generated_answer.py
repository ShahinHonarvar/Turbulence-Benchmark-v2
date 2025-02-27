from functools import reduce
            from math import sqrt

def all_left_right_truncatable_prime(n):
    x = n[84]

    def is_prime(n):
        return n > 1 and reduce(lambda x, y: x if y % x != 0 and y % x != 1 else y, range(2, int(sqrt(n)) + 1))
    primes = list(filter(is_prime, range(2, x + 1)))

    def left_truncatable(n):
        x = list(''.join(map(str, n)))
        if '0' in x:
            return False
        shift = len(x)
        for _ in range(len(x)):
            if len(x) < 2 and int(''.join(x)) > 1:
                return int(''.join(x))
            x.pop(0)

    def right_truncatable(n):
        x = list(''.join(map(str, n)))
        if '0' in x:
            return False
        shift = len(x)
        for _ in range(len(x)):
            if len(x) < 2 and int(''.join(x)) > 1:
                return int(''.join(x))
            x.pop(-1)
    lt = list(filter(left_truncatable, primes))
    rt = list(filter(right_truncatable, primes))
    lrt = list(filter(lambda x: x in lt and x in rt, primes))
    return sorted(lrt, reverse=True)