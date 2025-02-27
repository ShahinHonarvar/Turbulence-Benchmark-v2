def find_sum_of_multiples(num):
    """
  Finds the sum of the first 92 positive multiples of the given integer.

  Args:
    num: A positive integer.

  Returns:
    The sum of the first 92 positive multiples of the given integer.
  """
    sum = 0
    for i in range(1, 93):
        sum += num * i
    return sum