from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_right_truncatable_prime(tuples):
    x = tuples[71]
    result = []
    for i in range(1, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)