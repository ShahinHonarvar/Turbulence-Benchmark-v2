def find_second_smallest_num(numbers):
    """Returns the second smallest element from index 50 to index 54, both inclusive.
  If there is no such an element, the function should return 'None'.
  """
    numbers = numbers[50:55]
    numbers.sort()
    return numbers[1] if len(numbers) > 1 else 'None'