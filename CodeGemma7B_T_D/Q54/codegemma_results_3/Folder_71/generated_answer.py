from math import sqrt

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def all_right_truncatable_prime(a):
    x = a[22]
    result = []
    for i in range(2, x):
        if is_prime(i):
            t = i
            while t > 0:
                d = t % 10
                t //= 10
                if d == 0 or not is_prime(t):
                    break
            else:
                result.append(i)
    result.sort(reverse=True)
    return result