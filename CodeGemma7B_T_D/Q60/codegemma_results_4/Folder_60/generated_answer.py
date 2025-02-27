def is_prime(num):
    """
    Checks if a number is prime.

    Args:
    num: The number to check.

    Returns:
    True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    """
    Checks if a number is left-and-right-truncatable prime.

    Args:
    num: The number to check.

    Returns:
    True if num is left-and-right-truncatable prime, False otherwise.
    """
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        left = int(str_num[i:])
        right = int(str_num[:-i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    """
    Finds all left-and-right-truncatable prime numbers less than or equal to x.

    Args:
    nums: A tuple of positive integers.

    Returns:
    A list of left-and-right-truncatable prime numbers less than or equal to x.
    """
    x = nums[87]
    primes = []
    for num in range(1, x + 1):
        if is_truncatable_prime(num):
            primes.append(num)
    return primes