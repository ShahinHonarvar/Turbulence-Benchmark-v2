def find_divisors_in_range(num):
    """
  Finds all positive divisors of a number in the range of 11 to 41, both inclusive.

  Args:
    num: A positive integer.

  Returns:
    A list of positive divisors in the range of 11 to 41, or an empty list if no such divisors exist.
  """
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    divisors_in_range = []
    for divisor in divisors:
        if divisor in range(11, 42):
            divisors_in_range.append(divisor)
    return divisors_in_range