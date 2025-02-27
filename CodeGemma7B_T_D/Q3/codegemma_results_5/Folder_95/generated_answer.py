def all_pos_ints_inclusive(nums):
    """Returns all positive integers from index 82 to index 86, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    A list of positive integers from index 82 to index 86, inclusive, or an
    empty list if no such integers exist.
  """
    return [num for num in nums[82:87] if num > 0]