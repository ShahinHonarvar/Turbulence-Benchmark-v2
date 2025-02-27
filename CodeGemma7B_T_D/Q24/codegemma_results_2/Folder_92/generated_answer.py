def sum_of_divisors_in_range(n):
    """
            This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 8 and 9, both inclusive. If no such divisors exist in the specified range, the function should return 0.

            Args:
                n: A positive integer.

            Returns:
                The sum of all positive divisors of n that are between 8 and 9, both inclusive. If no such divisors exist, the function should return 0.
            """
    if n <= 8:
        return 0
    sum_of_divisors = 0
    for i in range(8, 10):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors