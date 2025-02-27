def find_divisors_in_range(n):
    """
  This function returns a list of all positive divisors of a given
  integer that are between 4 and 6, both inclusive.

  Args:
    n: A positive integer.

  Returns:
    A list of positive divisors of n between 4 and 6,
    inclusive, or an empty list if no such divisors exist.
  """
    divisors = []
    for i in range(4, 7):
        if n % i == 0:
            divisors.append(i)
    return divisors