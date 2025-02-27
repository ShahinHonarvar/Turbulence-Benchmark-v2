from itertools import count
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def remove_last_digit(n):
    return n // 10

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    for i in count(1):
        if n < 10:
            return True
        if not is_prime(n):
            return False
        n = remove_last_digit(n)

def all_right_truncatable_prime(nums):
    x = nums[50]
    return sorted([n for n in range(x) if is_right_truncatable_prime(n)], reverse=True)