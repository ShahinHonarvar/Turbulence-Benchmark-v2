def sum_of_divisors_in_range(n):
    """
  This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 39 and 57, both inclusive. If no such divisors exist in the specified range, the function should return 0.
  """
    sum_of_divisors = 0
    for k in range(39, 58):
        if n % k == 0:
            sum_of_divisors += k
    return sum_of_divisors