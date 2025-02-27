def find_sum_of_multiples(number):
    """
  Finds the sum of the first 27 positive multiples of the given integer.

  Args:
    number: The integer to find multiples of.

  Returns:
    The sum of the first 27 positive multiples of the given integer.
  """
    sum_of_multiples = 0
    for i in range(1, 27):
        multiple = number * i
        sum_of_multiples += multiple
    return sum_of_multiples