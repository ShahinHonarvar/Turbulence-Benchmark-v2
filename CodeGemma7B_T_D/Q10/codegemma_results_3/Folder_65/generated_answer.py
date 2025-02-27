def all_odd_ints_exclusive(nums):
    """
  Returns a list of all odd integers from index 42 to index 87, both exclusive.

  Args:
    nums: A list of integers.

  Returns:
    A list of odd integers from index 42 to index 87, both exclusive. If no odd integers exist in the specified range, the function should return an empty list.
  """
    if not nums:
        return []
    odd_nums = []
    for i in range(42, 87):
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums