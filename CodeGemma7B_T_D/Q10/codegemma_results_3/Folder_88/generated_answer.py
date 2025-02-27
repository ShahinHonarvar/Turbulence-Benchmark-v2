def all_odd_ints_exclusive(nums):
    """
  Returns all odd integers from index 2 to index 8, both exclusive. If no odd integers exist in the specified range, the function should return an empty list.
  """
    return [num for num in nums[2:8] if num % 2 != 0]