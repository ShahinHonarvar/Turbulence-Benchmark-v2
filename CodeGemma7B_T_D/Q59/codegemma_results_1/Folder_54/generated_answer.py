from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(tuple):
    result = []
    x = tuple[88]
    for num in range(2, x):
        if all((digit != '0' for digit in str(num))) and all((is_prime(int(str(num)[:i + 1])) for i in range(len(str(num))))):
            result.append(num)
    return sorted(result, reverse=True)