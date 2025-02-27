import math

def is_primes(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(x):
    result = [i for i in range(2, x) if is_primes(i) and all(is_primes((int(str(i)[:-j]) for j in range(1, len(str(i))))))]
    return sorted(result)