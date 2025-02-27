def find_divisors_in_range(n):
    """
  This function finds all positive divisors of the given integer that are between 84 and 86, both inclusive.
  If no such divisors exist in the specified range, the function should return an empty list.
  """
    divisors = []
    for i in range(84, 87):
        if n % i == 0:
            divisors.append(i)
    return divisors