import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[10]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            j = i
            while j > 1:
                j //= 10
                if not is_prime(j):
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)