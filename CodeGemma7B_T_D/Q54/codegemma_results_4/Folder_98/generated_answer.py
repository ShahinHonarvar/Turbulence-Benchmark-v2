from functools import reduce
from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, round(sqrt(n)) + 3, 2):
        if n % i == 0:
            return False
    return True

def num_to_string(n):
    if len(n) == 1:
        return str(n)
    return n[-1] + num_to_string(n[:-1])

def digit_sum(n):
    if len(n) == 1:
        return int(n)
    return int(n[-1]) + digit_sum(n[:-1])

def all_right_truncatable_prime(n):
    results = []
    x = n[8]
    for num in range(2, x):
        num_str = str(num)
        if is_prime(num):
            for i in range(1, len(num_str)):
                if not is_prime(digit_sum(num_str[i:])):
                    break
            else:
                results.append(num_str)
    return sorted(results, reverse=True)