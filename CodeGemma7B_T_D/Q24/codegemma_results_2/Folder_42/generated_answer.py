def sum_of_divisors_in_range(n):
    """Calculates the sum of positive divisors of n in the range [14, 93].

            Args:
              n: A positive integer.

            Returns:
              The sum of all positive divisors of n in the range [14, 93], or 0 if no such divisors exist.
            """
    sum = 0
    for divisor in range(14, 94):
        if n % divisor == 0:
            sum += divisor
    return sum