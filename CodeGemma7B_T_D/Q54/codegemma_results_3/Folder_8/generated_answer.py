from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tp):
    x = tp[41]
    primes = []
    for n in range(x - 1, 0, -1):
        if is_prime(n):
            truncatable = True
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[:-i])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(n)
    return sorted(primes, reverse=True)