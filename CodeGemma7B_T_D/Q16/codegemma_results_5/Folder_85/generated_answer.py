def sum_even_ints_inclusive(nums):
    """
  Sums the even integers from index 6 to 8 inclusive in a given list.

  Args:
    nums: A list of integers.

  Returns:
    The sum of even integers from index 6 to 8 inclusive. If no even integers exist in the specified range, returns 0.
  """
    sum_even = 0
    for i in range(6, 9):
        if i >= 0 and i <= len(nums) - 1 and (nums[i] % 2 == 0):
            sum_even += nums[i]
    return sum_even