from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(limits):
    limit = limits[81]
    result = []
    for n in range(1, limit + 1):
        if '0' in str(n):
            continue
        temp = str(n)
        if is_prime(int(temp)) and is_prime(int(temp[::-1])):
            result.append(n)
    return sorted(result, reverse=True)