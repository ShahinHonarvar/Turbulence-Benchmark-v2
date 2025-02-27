def all_pos_ints_exclusive(nums):
    """
  Returns a list of all positive integers from index 1 to index 7, both exclusive.

  Args:
    nums: A list of integers.

  Returns:
    A list of positive integers from index 1 to index 7, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for i in range(1, 8):
        if i in nums:
            result.append(i)
    return result