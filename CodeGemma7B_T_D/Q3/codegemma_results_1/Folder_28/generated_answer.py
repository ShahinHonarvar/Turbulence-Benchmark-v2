def all_pos_ints_inclusive(nums):
    """
  Returns a list of all positive integers from index 62 to index 63, both inclusive.
  If no positive integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for i in range(62, 64):
        if i >= 0 and i <= len(nums) - 1 and (nums[i] > 0):
            result.append(nums[i])
    return result