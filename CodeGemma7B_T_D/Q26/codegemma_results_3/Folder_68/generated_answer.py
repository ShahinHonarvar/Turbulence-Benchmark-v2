def sum_in_range(nums):
    """
  Sums all integers from a list that are between 7 and 9, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of all integers in the list between 7 and 9, inclusive. 0 if the given list does not contain such integers.
  """
    sum_in_range = 0
    for num in nums:
        if 7 <= num <= 9:
            sum_in_range += num
    return sum_in_range