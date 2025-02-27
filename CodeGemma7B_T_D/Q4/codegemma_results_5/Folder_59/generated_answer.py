def all_pos_ints_exclusive(nums):
    """
  Write a function called 'all_pos_ints_exclusive' that takes one argument, a list of integers, and returns the list of all positive integers from index 0 to index 9, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
  """
    return [num for num in nums if num > 0 and num < 10]