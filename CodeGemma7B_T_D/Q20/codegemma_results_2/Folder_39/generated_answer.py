def find_n_th_smallest_num(nums):
    """
  Finds the 7th smallest number from index 47 to index 89, both inclusive.

  Args:
    nums: A list of distinct numbers.

  Returns:
    The 7th smallest number from index 47 to index 89, both inclusive.
  """
    nums.sort()
    return nums[47:89][6]