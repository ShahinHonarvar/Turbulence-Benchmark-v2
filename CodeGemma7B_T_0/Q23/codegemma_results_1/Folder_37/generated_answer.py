def find_divisors_in_range(num):
    """
  This function takes a positive integer as its argument, and returns the list of all positive divisors of the given integer that are between 3 and 7, both inclusive. If no such divisors exist in the specified range, the function should return an empty list.
  """
    divisors = []
    for i in range(3, 8):
        if num % i == 0:
            divisors.append(i)
    return divisors