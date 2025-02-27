def sum_even_ints_inclusive(nums):
    """
  Sums all even integers from index 50 to index 54, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of all even integers from index 50 to index 54, inclusive. If no even integers exist in the specified range, the function should return 0.
  """
    sum_even_nums = 0
    for i in range(50, 55):
        if i >= 0 and i <= len(nums) - 1 and (nums[i] % 2 == 0):
            sum_even_nums += nums[i]
    return sum_even_nums