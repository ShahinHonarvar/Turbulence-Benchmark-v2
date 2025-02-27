def sum_of_divisors_in_range(n):
    """
            This function takes a positive integer `n` and returns
            the sum of all positive divisors of `n` that are
            between 14 and 93, inclusive. If no such divisors
            exist in the specified range, the function returns 0.

            Args:
            n: A positive integer.

            Returns:
            The sum of all positive divisors of `n` that are
            between 14 and 93, inclusive.
            """
    sum = 0
    for i in range(14, 93 + 1):
        if n % i == 0:
            sum += i
    return sum