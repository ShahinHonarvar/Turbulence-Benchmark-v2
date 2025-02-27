import itertools
import re

def all_right_truncatable_prime(test_tup):
    x = test_tup[2]
    gen = (p for p in range(2, x) if all((int(d) for d in str(p) if d != '0')))
    res = list(filter(lambda p: all((int(d) for d in str(p))), gen))
    res.sort(reverse=True)
    return res