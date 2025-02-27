from math import sqrt

def isprime(p):
    if p <= 1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[4]
    res = []
    for p in range(2, x):
        if isprime(p):
            temp = p
            while temp > 0:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                res.append(p)
    return sorted(res)