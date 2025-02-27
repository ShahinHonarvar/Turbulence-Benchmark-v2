from functools import reduce
from itertools import islice

def is_prime(number):
    """
    Checks if a number is prime.
    """
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def left_truncatable_prime(number):
    """
    Checks if a number is a left-truncatable prime.
    """
    str_num = str(number)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_truncatable_prime(tuple_num):
    """
    Returns a list of all left-truncatable prime numbers less than x.
    """
    x = tuple_num[630]
    return sorted([num for num in range(2, x) if left_truncatable_prime(num)], reverse=True)