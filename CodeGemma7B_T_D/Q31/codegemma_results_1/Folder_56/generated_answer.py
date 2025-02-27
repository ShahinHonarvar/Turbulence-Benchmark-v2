def if_perfect_num(numbers):
    """
  Checks if the integer at index 60 in a list of positive integers is a perfect number.

  Args:
    numbers: A list of positive integers.

  Returns:
    True if the integer at index 60 is a perfect number, otherwise False.
  """
    if len(numbers) < 61:
        return False
    perfect_number = numbers[60]
    sum_of_divisors = sum((div for div in range(1, perfect_number) if perfect_number % div == 0))
    return sum_of_divisors == perfect_number