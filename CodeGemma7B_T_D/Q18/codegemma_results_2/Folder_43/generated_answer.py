def sum_ints_div_by_either_nums(nums):
    """
  Sums all integers divisible by either -77 or -32 from index 57 to index 85, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of all integers divisible by either -77 or -32 from index 57 to index 85, inclusive. If no such integers exist in the specified range, the function should return 0.
  """
    divisible_count = 0
    sum_values = 0
    for i in range(57, 86):
        if nums[i] % -77 == 0 or nums[i] % -32 == 0:
            sum_values += nums[i]
            divisible_count += 1
    if divisible_count == 0:
        return 0
    return sum_values