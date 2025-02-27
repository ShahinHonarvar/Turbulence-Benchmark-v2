def all_odd_ints_exclusive(nums):
    """
  Creates and returns a list of all odd integers in the range [362, 642) from a given list.

  Args:
    nums: A list of integers.

  Returns:
    A list of all odd integers in the range [362, 642) from `nums` or an empty list if no such integers exist.
  """
    odd_nums = []
    for i in range(362, 642):
        if i % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums