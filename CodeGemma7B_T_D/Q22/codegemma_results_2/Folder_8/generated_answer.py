def find_sum_of_multiples(argument):
    """
  This function takes one argument, a positive integer, and returns the sum of the first 53 possitive multiples of the given integer.
  """
    sum_of_multiples = 0
    for i in range(1, 54):
        sum_of_multiples += argument * i
    return sum_of_multiples