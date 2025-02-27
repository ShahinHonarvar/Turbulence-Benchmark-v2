def sum_of_divisors_in_range(n):
    """
            This function takes a positive integer as its argument, and returns the sum of all
            positive divisors of the given integer that are between 27 and 44, both inclusive.
            If no such divisors exist in the specified range, the function should return 0.

            Args:
                n: A positive integer.

            Returns:
                The sum of all positive divisors of the given integer that are between 27 and 44,
                both inclusive. If no such divisors exist in the specified range, the function
                should return 0.
            """
    total_sum = 0
    for i in range(27, 45):
        if n % i == 0:
            total_sum += i
    if total_sum == 0:
        return 0
    else:
        return total_sum