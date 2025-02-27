from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[19]
    result = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            num = i
            while num != 0:
                if not is_prime(num):
                    truncatable = False
                    break
                num //= 10
            if truncatable:
                result.append(i)
    return sorted(result)