def sum_of_divisors_in_range(n):
    """
  This function returns the sum of all positive divisors of the given integer that are between 10 and 69, both inclusive. If no such divisors exist in the specified range, the function should return 0.
  """
    sum_of_divisors = 0
    for i in range(10, 70):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors