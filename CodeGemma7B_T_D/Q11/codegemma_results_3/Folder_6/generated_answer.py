def find_largest_num(nums):
    """
  Finds the largest element from index 10 to index 66, both inclusive.

  Args:
    nums: A list of numbers.

  Returns:
    The largest element from index 10 to index 66, both inclusive.
  """
    largest_num = float('-inf')
    for num in nums[10:67]:
        if num > largest_num:
            largest_num = num
    return largest_num