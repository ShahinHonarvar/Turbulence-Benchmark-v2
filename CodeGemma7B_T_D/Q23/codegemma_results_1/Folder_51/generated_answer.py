def find_divisors_in_range(number):
    """
  This function takes a positive integer as its argument and returns the list of all positive divisors
  of the given integer that are between 2 and 7, both inclusive. If no such divisors exist in the
  specified range, the function should return an empty list.
  """
    return [factor for factor in range(2, 8) if number % factor == 0]