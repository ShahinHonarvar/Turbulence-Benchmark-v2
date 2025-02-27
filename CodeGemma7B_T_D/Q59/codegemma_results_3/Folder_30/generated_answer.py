from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    result = []
    for i in range(2, x):
        if str(i) not in '0' and all_prime(str(i)) and all_prime([int(a) for a in str(i)]) and all_prime([int(a) for a in str(i)[1:]]):
            result.append(i)
    return sorted(result)[::-1]

def all_prime(n):
    for i in n:
        if not is_prime(i):
            return False
    return True