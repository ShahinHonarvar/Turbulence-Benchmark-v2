from math import sqrt

def all_left_truncatable_prime(n):
    result = []
    for i in range(1, n):
        if left_truncatable_prime(i):
            result.append(i)
    return sorted(result)