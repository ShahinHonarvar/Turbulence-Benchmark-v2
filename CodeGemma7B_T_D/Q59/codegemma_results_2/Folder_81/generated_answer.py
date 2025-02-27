from math import sqrt
from itertools import combinations_with_replacement

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[98]
    result = []
    for i in range(2, x):
        if is_prime(i):
            for j in range(i):
                if i * 10 ** j + j in result:
                    break
            else:
                result.append(i)
    return sorted(result)