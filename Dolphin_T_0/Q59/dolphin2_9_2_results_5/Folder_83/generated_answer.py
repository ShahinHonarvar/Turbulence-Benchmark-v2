import itertools
import math

def all_left_truncatable_prime(n):
    to_list = list(n)
    limit_int = to_list[24]
    left_truncatable_primes = []
    for i in range(2, limit_int + 1):
        if is_prime(i):
            if all((is_prime(int(''.join(x))) for x in itertools.combinations(str(i), 1))):
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True