def is_prime(num):
    """
    Checks if a given integer is prime.

    Args:
    num: The integer to check.

    Returns:
    True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    """
    Checks if a given integer is a left-truncatable prime.

    Args:
    num: The integer to check.

    Returns:
    True if num is a left-truncatable prime, False otherwise.
    """
    str_num = str(num)
    for i in range(1, len(str_num)):
        truncatable_num = int(str_num[i:])
        if not is_prime(truncatable_num):
            return False
    return True

def all_left_truncatable_prime(tuple):
    """
    Returns the list of all left-truncatable prime numbers less than x.

    Args:
    tuple: A tuple of positive integers.

    Returns:
    A list of left-truncatable prime numbers less than x, sorted in descending order.
    """
    result = []
    for num in tuple:
        if left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)