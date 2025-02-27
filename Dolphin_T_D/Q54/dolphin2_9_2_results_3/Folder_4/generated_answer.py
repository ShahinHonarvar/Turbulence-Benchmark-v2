import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[96]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            if i >= 10:
                s = str(i)
                for j in range(len(s) - 1, 0, -1):
                    if not is_prime(int(s[:j])):
                        break
                else:
                    primes.append(i)
    return sorted(primes, reverse=True)