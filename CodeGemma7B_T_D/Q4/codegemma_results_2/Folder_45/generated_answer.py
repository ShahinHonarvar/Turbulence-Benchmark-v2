def all_pos_ints_exclusive(nums):
    """
  Returns a list of all positive integers from index 30 to index 200, both exclusive.

  Args:
    nums: A list of integers.

  Returns:
    A list of positive integers from index 30 to index 200, both exclusive. If no positive integers exist in the specified range, the function returns an empty list.
  """
    pos_ints = []
    for i in range(30, 200):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints