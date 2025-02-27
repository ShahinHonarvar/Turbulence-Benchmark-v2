def sum_ints_div_by_either_nums(nums):
    """
  Sums integers divisible by either -9 or -7 in a list from index 7 to 9.

  Args:
    nums: A list of integers.

  Returns:
    The sum of integers divisible by either -9 or -7, or 0 if no such integers exist.
  """
    sum = 0
    for num in nums[7:10]:
        if num % -9 == 0 or num % -7 == 0:
            sum += num
    return sum