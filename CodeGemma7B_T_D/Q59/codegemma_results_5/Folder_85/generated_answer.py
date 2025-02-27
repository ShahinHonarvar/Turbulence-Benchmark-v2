import math
import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    result = []
    for i in range(2, x - 1):
        str_i = str(i)
        if '0' not in str_i and is_prime(i):
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[j:])):
                    break
            else:
                result.append(i)
    return result