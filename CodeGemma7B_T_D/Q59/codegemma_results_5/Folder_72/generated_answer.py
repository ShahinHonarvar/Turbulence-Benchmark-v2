from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[31]
    result = []
    for n in range(x - 1, 1, -1):
        if n % 10 == 0:
            continue
        if is_prime(n):
            is_truncatable = True
            num = n
            while num > 0:
                num //= 10
                if num == 0 or not is_prime(num):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(n)
    return result