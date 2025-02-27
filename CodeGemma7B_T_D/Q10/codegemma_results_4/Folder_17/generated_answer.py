def all_odd_ints_exclusive(nums):
    """
  Args:
    nums: list of integers

  Returns:
    list of odd integers from index 62 to index 96, both exclusive.
    If no odd integers exist in the specified range, the function returns an empty list.
  """
    if not nums:
        return []
    odd_nums = []
    for i in range(62, 97):
        if i % 2 != 0 and i in range(63, 97):
            odd_nums.append(nums[i])
    return odd_nums