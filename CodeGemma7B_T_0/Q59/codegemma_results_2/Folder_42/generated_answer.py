def all_left_truncatable_prime(t):
    x = t[64]
    res = []
    for i in range(2, x):
        if isprime(i) and (not haszero(i)) and islefttruncatableprime(i):
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

def islefttruncatableprime(i):
    str_i = str(i)
    for j in range(1, len(str_i)):
        if not isprime(int(str_i[j:])):
            return False
    return True