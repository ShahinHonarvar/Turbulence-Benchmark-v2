from math import *

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(args):
    x = args[69]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        if '0' not in prime_str:
            is_left_truncatable = True
            for i in range(1, len(prime_str)):
                if not is_prime(int(prime_str[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)