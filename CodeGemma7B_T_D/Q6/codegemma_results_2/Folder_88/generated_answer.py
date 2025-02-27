def all_neg_ints_exclusive(nums):
    """
  Returns a list of all negative integers from index 2 to index 8 (exclusive).
  If no negative integers exist in the specified range, an empty list is returned.
  """
    result = []
    for i in range(2, 8):
        if nums[i] < 0:
            result.append(nums[i])
    return result