from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[81]
    primes = [i for i in range(2, x) if is_prime(i)]
    prime_str = [str(p) for p in primes]
    results = []
    for pstr in prime_str:
        for i in range(1, len(pstr)):
            num = int(pstr[:-i])
            if num not in primes:
                break
        else:
            results.append(int(pstr))
    return sorted(results, reverse=True)