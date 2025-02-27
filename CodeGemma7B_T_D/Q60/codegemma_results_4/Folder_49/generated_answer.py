from math import sqrt
from itertools import count

def is_prime(n):
    """
    This function checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    """
    This function returns a list of left-and-right-truncatable prime numbers less than or equal to x.
    """

    def helper(x):
        """
        This helper function checks if a number is a left-and-right-truncatable prime number.
        """
        if x <= 1 or '0' in str(x):
            return False
        for i in range(1, len(str(x))):
            if not is_prime(int(str(x)[:i])) or not is_prime(int(str(x)[-i:])):
                return False
        return True
    result = []
    for num in nums:
        if helper(num):
            result.append(num)
    result.sort()
    return result