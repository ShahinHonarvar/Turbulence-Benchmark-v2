def all_pos_ints_inclusive(nums):
    """
  Returns a list of all positive integers from index 23 to index 23, both inclusive.
  If no positive integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for i in range(23, 24):
        if i >= 0:
            result.append(nums[i])
    return result