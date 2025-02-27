def sum_of_divisors_in_range(n):
    """
    Function to calculate the sum of all positive divisors of a given integer n that are between 50 and 81, both inclusive.
    If no such divisors exist in the specified range, the function returns 0.
    """
    result = 0
    for i in range(50, 82):
        if n % i == 0:
            result += i
    return result