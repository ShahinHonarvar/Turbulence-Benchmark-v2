def sum_of_divisors_in_range(num):
    """
  This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 40 and 74, both inclusive. If no such divisors exist in the specified range, the function should return 0.


  >>> print(sum_of_divisors_in_range(3))
  4
  >>> print(sum_of_divisors_in_range(6))
  9
  >>> print(sum_of_divisors_in_range(10))
  12
  """
    sum_of_divisors = 0
    for i in range(40, 75):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors