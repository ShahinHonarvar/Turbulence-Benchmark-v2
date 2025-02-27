from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[992]
    result = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                result.append(num)
                num //= 10
    result.sort()
    return result