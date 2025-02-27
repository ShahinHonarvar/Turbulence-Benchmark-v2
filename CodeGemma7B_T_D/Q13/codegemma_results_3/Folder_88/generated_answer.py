def find_second_largest_num(nums):
    """
  Finds the second largest element from index 4 to index 8, both inclusive. If there is no such element, the function returns 'None'.

  Args:
    nums: A list of distinct numbers.

  Returns:
    The second largest element from index 4 to index 8, both inclusive, or 'None' if there is no such element.
  """
    if len(nums) == 0:
        return None
    nums.sort(reverse=True)
    if 4 <= len(nums) <= 8:
        return nums[4]
    else:
        return None