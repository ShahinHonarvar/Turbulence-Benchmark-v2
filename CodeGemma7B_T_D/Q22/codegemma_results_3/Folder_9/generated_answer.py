def find_sum_of_multiples(num):
    """
  This function finds the sum of the first 68 possitive multiples of the given integer.

  Args:
    num: A positive integer.

  Returns:
    The sum of the first 68 possitive multiples of the given integer.
  """
    multiples = range(1, 69)
    return sum([multiple * num for multiple in multiples])