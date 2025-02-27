def all_ints_not_div_by_num(nums):
    """
  Returns a list of all integers not divisible by -46 from index 22 to index 97, both exclusive.

  Args:
    nums: A list of integers.

  Returns:
    A list of integers not divisible by -46 from index 22 to index 97, both exclusive. If no such integers exist, an empty list is returned.
  """
    filtered_nums = [num for num in nums[22:97] if num % -46 != 0]
    return filtered_nums or []