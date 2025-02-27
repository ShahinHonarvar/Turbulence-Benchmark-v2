import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[55]
    res = []
    for i in range(10 ** (len(str(x)) - 1), x):
        if is_prime(i) and all((is_prime(int(str(i)[:-k])) for k in range(1, len(str(i))))):
            res.append(i)
    return sorted(res, reverse=True)