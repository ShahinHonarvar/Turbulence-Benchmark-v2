def find_divisors_in_range(num):
    """
  Finds all positive divisors of a number in a given range.

  Parameters:
    num: The number to find divisors for.

  Returns:
    A list of positive divisors of the given number that are between 18 and 52, both inclusive. If no such divisors exist, an empty list is returned.
  """
    divisors = []
    for i in range(18, 53):
        if num % i == 0:
            divisors.append(i)
    return divisors