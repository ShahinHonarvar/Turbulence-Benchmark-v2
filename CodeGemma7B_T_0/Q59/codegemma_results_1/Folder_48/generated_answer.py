def all_left_truncatable_prime(t):
    x = t[835]
    res = []
    for i in range(2, x):
        if isprime(i) and (not '0' in str(i)):
            if islefttruncatableprime(i):
                res.append(i)
    res.sort()
    return res

def isprime(i):
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def islefttruncatableprime(i):
    if not isprime(i):
        return False
    for j in range(len(str(i)) - 1):
        if not isprime(int(str(i)[j + 1:])):
            return False
    return True