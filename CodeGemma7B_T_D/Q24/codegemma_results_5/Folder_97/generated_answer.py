def sum_of_divisors_in_range(x):
    """
            Args:
                x: A positive integer.

            Returns:
                The sum of all positive divisors of x in the specified range [615, 792].
            If no such divisors exist, returns 0.
            """
    for n in range(615, 793):
        if x % n == 0:
            sum_of_divisors_in_range += n
    return sum_of_divisors_in_range