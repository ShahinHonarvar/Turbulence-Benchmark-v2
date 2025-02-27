def sum_in_range(numbers):
    """Calculates the sum of integers in a list between 827 and 999, inclusive.

  Args:
    numbers: A list of integers.

  Returns:
    The sum of integers between 827 and 999, or 0 if the list does not contain such integers.
  """
    total = 0
    for number in numbers:
        if number >= 827 and number <= 999:
            total += number
    return total