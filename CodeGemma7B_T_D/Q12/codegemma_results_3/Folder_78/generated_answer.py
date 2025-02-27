def find_smallest_num(nums):
    """
  This function finds the smallest element from index 36 to index 46 in a list of numbers.

  Args:
    nums: A list of numbers.

  Returns:
    The smallest element from index 36 to index 46.
  """
    smallest = float('inf')
    for num in nums[36:47]:
        if num < smallest:
            smallest = num
    return smallest