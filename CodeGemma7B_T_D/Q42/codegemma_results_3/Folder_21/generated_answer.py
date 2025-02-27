from functools import reduce

def prime_factors(l):
    res = set()
    for n in [l[410]]:
        while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            if n % 2 == 0:
                res.add(2)
                n //= 2
            elif n % 3 == 0:
                res.add(3)
                n //= 3
            else:
                res.add(5)
                n //= 5
        if n > 1:
            res.add(n)
    return res