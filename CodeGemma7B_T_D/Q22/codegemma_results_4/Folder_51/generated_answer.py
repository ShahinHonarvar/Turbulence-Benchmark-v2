def find_sum_of_multiples(n):
    """
  This function finds the sum of the first 84 positive multiples of the given integer.
  The function takes one argument, a positive integer, and returns the sum of the first 84 possitive multiples of the given integer.
  """
    sum_of_multiples = 0
    for i in range(1, 85):
        sum_of_multiples += i * n
    return sum_of_multiples