def find_sum_of_multiples(n):
    """
  Calculates the sum of the first 223 positive multiples of a given integer.
  
  Args:
    n: The integer to find multiples of.

  Returns:
    The sum of the first 223 positive multiples of n.
  """
    multiples = []
    i = 1
    while len(multiples) < 223:
        multiple = n * i
        multiples.append(multiple)
        i += 1
    return sum(multiples)