import sys
from functools import reduce

def all_left_truncatable_prime(test_tup):
    if test_tup[10] > 10 ** 4:
        return []
    primes = []
    for n in range(3, int(test_tup[10]) + 1):
        if all((n % d != 0 for d in range(2, int(str(n)[0])))):
            primes.append((n, [n]))
            for i in range(2, int(str(n)[0]) + 1):
                primes += [(n - int(str(n)[0]), [n - int(str(n)[0])])]
    return reduce(lambda acc, cur: acc + cur[1], primes)