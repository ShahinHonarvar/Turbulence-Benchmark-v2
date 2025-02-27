def all_left_truncatable_prime(tup):
    x = tup[76]
    res = []
    for i in range(2, x):
        if isprime(i):
            if islefttruncatableprime(i):
                res.append(i)
    res.sort(reverse=True)
    return res

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def islefttruncatableprime(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not isprime(int(str(n)[i:])):
            return False
    return True