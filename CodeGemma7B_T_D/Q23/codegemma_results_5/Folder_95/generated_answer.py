def find_divisors_in_range(x):
    """
  The function 'find_divisors_in_range' takes a positive integer as an argument and
  returns the list of all positive divisors of the number that lie between 35 and
  98, both inclusive. If no such divisors are found, the function returns an empty list.
  """
    divisors_in_range = []
    for i in range(35, 99):
        if x % i == 0:
            divisors_in_range.append(i)
    return divisors_in_range