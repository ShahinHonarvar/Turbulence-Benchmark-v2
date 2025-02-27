from math import sqrt

def left_truncatable_prime(num):
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    if num <= 1 or '0' in str(num):
        return False
    return True

def right_truncatable_prime(num):
    return left_truncatable_prime(int(str(num)[:-1]))

def all_left_right_truncatable_prime(tup):
    x = tup[70]
    result = []
    for num in range(3, x + 1, 2):
        if left_truncatable_prime(num) and right_truncatable_prime(num):
            result.append(num)
    return result