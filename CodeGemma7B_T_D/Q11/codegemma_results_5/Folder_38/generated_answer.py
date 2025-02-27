def find_largest_num(numbers):
    """
  Finds the largest element in a list from index 22 to index 63, inclusive.

  Args:
    numbers: A list of numbers.

  Returns:
    The largest element from index 22 to index 63, inclusive.
  """
    largest_num = numbers[22]
    for num in numbers[23:64]:
        if num > largest_num:
            largest_num = num
    return largest_num