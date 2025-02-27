def find_divisors_in_range(num):
    """
  Finds all positive divisors of a number in a given range.

  Args:
    num: The number to find divisors of.

  Returns:
    A list of all positive divisors of the given number in the range [28, 81], inclusive, or an empty list if no such divisors exist.
  """
    'Return an empty list if the input number is zero or negative.'
    if num <= 0:
        return []
    'Initialize a list to store the divisors.'
    divisors = []
    'Iterate over all numbers in the range [28, 81].'
    for i in range(28, 82):
        'Check if the number is a divisor of the input number.'
        if num % i == 0:
            'If it is, add it to the list of divisors.'
            divisors.append(i)
    return divisors