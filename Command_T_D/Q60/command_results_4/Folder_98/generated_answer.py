import itertools
import re
import functools

@functools.lru_cache(maxsize=1000000)
def is_left_right_truncatable_prime(n):
    s = str(n)
    while s[0] != '1':
        s = s[1:]
    while s[-1] != '1' and s[-2] != '2':
        s = s[:-1]
    return n in PRIME and PRIMES_RE.match(s)

def all_left_right_truncatable_prime(n):
    it = itertools.takewhile(lambda x: x <= n and is_left_right_truncatable_prime(x), PRIMES)
    return sorted(filter(lambda x: x in range(2, n + 1), it))