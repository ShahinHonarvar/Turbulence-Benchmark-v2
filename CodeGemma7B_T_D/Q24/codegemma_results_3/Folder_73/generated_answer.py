def sum_of_divisors_in_range(x):
    """
  This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 46 and 89, both inclusive. If no such divisors exist in the specified range, the function should return 0.
  """
    sum_of_divisors = 0
    for i in range(46, 89 + 1):
        if x % i == 0:
            sum_of_divisors += i
    return sum_of_divisors