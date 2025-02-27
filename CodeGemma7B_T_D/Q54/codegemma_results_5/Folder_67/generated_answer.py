from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[71]
    res = []
    for i in reversed(range(2, x)):
        if is_prime(i):
            temp = i
            while temp > 1:
                temp //= 10
                if not is_prime(temp):
                    break
            else:
                res.append(i)
    return sorted(res, reverse=True)