def sum_of_divisors_in_range(num):
    """
  Sums the positive divisors of a number between 43 and 77, inclusive.

  Args:
    num: The number to find divisors of.

  Returns:
    The sum of the positive divisors between 43 and 77, or 0 if no such divisors exist.
  """
    sum_of_divisors = 0
    for divisor in range(43, 78):
        if num % divisor == 0:
            sum_of_divisors += divisor
    if sum_of_divisors == 0:
        return 0
    return sum_of_divisors