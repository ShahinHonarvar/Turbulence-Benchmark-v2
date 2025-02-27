import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[35]
    primes = [i for i in range(x, -1, -1) if is_prime(i)]
    truncatables = []
    for prime in primes:
        k = prime
        while k > 1:
            k = int(str(k)[1:])
            if not is_prime(k) or k == 0:
                break
        else:
            truncatables.append(prime)
    return truncatables