def sum_of_divisors_in_range(n):
    """
    The function returns the sum of all positive divisors of the given integer n
    that are between 43 and 46, both inclusive. If no such divisors exist in
    the specified range, the function returns 0.
    """
    sum_of_divisors = 0
    for i in range(43, 47):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors