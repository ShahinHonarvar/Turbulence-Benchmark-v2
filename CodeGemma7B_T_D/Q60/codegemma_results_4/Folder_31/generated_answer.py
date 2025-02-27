from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and (not str(i).count('0')) and is_prime(i // 10 ** (len(str(i)) - 1)):
            result.append(i)
    result.sort(reverse=True)
    return result