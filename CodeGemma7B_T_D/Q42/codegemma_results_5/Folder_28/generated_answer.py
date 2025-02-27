from math import sqrt

def prime_factors(lst):
    res = set()
    for i in range(2, int(sqrt(lst[37])) + 1):
        if lst[37] % i == 0:
            res.add(i)
    return res