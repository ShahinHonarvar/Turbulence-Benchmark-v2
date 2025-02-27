def sum_in_range(nums):
    """
  Sums all integers from the given list that are between 5 and 9, both inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of integers from the given list that are between 5 and 9, both inclusive. If the given list does not contain such integers, the function should return 0.
  """
    count = 0
    for num in nums:
        if num >= 5 and num <= 9:
            count += num
    return count