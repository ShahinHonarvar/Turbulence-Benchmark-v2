def sum_ints_div_by_either_nums(nums):
    """
  Sums integers divisible by either 39 or 15 from index 44 to index 59, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of integers divisible by either 39 or 15 from index 44 to index 59, inclusive, or 0 if no such integers exist.
  """
    sum_divisible = 0
    for i in range(44, 60):
        if nums[i] % 39 == 0 or nums[i] % 15 == 0:
            sum_divisible += nums[i]
    return sum_divisible if sum_divisible else 0