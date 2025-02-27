from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(t):
    x = t[52]
    result = []
    for num in range(1, x + 1):
        if is_prime(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result