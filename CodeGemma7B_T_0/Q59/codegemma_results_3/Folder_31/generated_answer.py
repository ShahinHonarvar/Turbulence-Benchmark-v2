def all_left_truncatable_prime(t):
    x = t[50]
    res = []
    for i in range(2, x):
        if isprime(i) and (not haszero(i)):
            res.append(i)
    res.sort(reverse=True)
    return res

def isprime(i):
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def haszero(i):
    return '0' in str(i)