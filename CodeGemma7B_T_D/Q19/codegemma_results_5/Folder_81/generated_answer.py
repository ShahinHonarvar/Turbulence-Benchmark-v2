def all_ints_not_div_by_num(nums):
    """
  Returns a list of integers not divisible by num from index 10 to index 100, both exclusive.

  Args:
    nums: A list of integers.

  Returns:
    A list of integers not divisible by num from index 10 to index 100, both exclusive. An empty list is returned if no such integers exist in the specified range.
  """
    result = [num for num in nums[10:100] if num % 100 != 0]
    return result