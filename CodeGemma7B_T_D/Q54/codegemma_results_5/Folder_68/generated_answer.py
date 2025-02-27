from math import sqrt

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    result = []
    for i in range(2, n):
        a = i
        if is_prime(a):
            while a > 0:
                if not is_prime(a):
                    break
                a = int(str(a)[:-1])
            else:
                result.append(i)
    return sorted(result, reverse=True)