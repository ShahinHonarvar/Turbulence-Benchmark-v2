def all_pos_ints_exclusive(nums):
    """
  :type nums: List[int]
  :rtype: List[int]
  """
    res = []
    for i in range(276, 376):
        if i >= 0 and i < len(nums) and (nums[i] > 0):
            res.append(nums[i])
    return res