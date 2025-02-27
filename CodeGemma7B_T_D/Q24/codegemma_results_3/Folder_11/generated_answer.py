def sum_of_divisors_in_range(n):
    """ 
            This function takes a positive integer as input and returns the sum of all positive divisors of the given integer that are between 39 and 57, both inclusive. If no such divisors exist in the specified range, the function should return 0.

            Args:
                n: A positive integer.

            Returns:
                The sum of all positive divisors of the given integer that are between 39 and 57, both inclusive. If no such divisors exist in the specified range, the function should return 0.
            """
    sum_of_divisors = 0
    for i in range(39, 58):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors