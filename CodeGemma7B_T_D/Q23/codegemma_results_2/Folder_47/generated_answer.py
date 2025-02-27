def find_divisors_in_range(num):
    """
  Finds all positive divisors of a number between 27 and 44, inclusive.

  Args:
    num: The number to find divisors for.

  Returns:
    A list of all positive divisors of num between 27 and 44, inclusive. An empty list if no such divisors exist.
  """
    if num <= 0:
        raise ValueError('Number must be positive.')
    divisors = []
    for i in range(27, 45):
        if num % i == 0:
            divisors.append(i)
    return divisors