def find_divisors_in_range(num):
    """
  This function finds all positive divisors of a given number that are between 586 and 840, both inclusive.

  Args:
    num: The number to find divisors of.

  Returns:
    A list of positive divisors that are between 586 and 840, both inclusive.
    If no such divisors exist in the specified range, an empty list is returned.
  """
    divisors = []
    for i in range(586, 841):
        if num % i == 0:
            divisors.append(i)
    return divisors