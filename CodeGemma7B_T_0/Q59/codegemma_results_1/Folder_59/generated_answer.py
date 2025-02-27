def all_left_truncatable_prime(tup):
    x = tup[84]
    res = []
    for i in range(2, x):
        if isprime(i):
            if islefttruncatableprime(i):
                res.append(i)
    res.sort(reverse=True)
    return res

def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def islefttruncatableprime(num):
    strnum = str(num)
    if '0' in strnum:
        return False
    for i in range(1, len(strnum)):
        if not isprime(int(strnum[i:])):
            return False
    return True