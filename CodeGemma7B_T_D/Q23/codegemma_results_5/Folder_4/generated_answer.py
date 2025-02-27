def find_divisors_in_range(num):
    """
  Finds all positive divisors of a given integer that are between 48 and 60, both inclusive.

  Args:
    num: The integer to find divisors of.

  Returns:
    A list of positive divisors in the specified range, or an empty list if no such divisors exist.
  """
    divisors = []
    for divisor in range(48, 61):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors