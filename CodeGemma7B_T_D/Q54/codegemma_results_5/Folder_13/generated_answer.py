from math import log, sqrt

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(a):
    x = a[784]
    res = []
    for i in range(2, x):
        if prime(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not prime(int(str_i[:-j])):
                    break
            else:
                res.append(i)
    res.sort()
    return res