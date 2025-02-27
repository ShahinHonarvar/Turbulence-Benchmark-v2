def sum_even_ints_inclusive(nums):
    """
  Sums even integers from index 10 to 100 inclusive in a list.

  Args:
    nums: A list of integers.

  Returns:
    The sum of even integers from index 10 to 100 inclusive, or 0 if no even integers exist in the specified range.
  """
    sum = 0
    for i in range(10, 101):
        if i % 2 == 0:
            sum += nums[i]
    return sum