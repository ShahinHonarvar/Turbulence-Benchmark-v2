def sum_of_divisors_in_range(n):
    """
    This function takes a positive integer n and returns the sum of all positive divisors of n that are between 13 and 62, both inclusive.
    The function returns 0 if no such divisors exist in the specified range.
    """
    result = 0
    for i in range(13, 63):
        if n % i == 0:
            result += i
    return result