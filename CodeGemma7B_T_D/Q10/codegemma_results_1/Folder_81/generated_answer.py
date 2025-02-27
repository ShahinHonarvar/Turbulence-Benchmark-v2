def all_odd_ints_exclusive(numbers):
    """
  Write a function called 'all_odd_ints_exclusive' that takes one argument, a list of integers, and returns the list of all odd integers from index 10 to index 11, both exclusive. If no odd integers exist in the specified range, the function should return an empty list.
  """
    return [num for num in numbers[10:11] if num % 2 != 0]