def sum_in_range(nums):
    """
  Sums all integers from a list of integers between 3 and 6, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of all integers from the list that are between 3 and 6, inclusive. If
    the list does not contain such integers, 0 is returned.
  """
    sum = 0
    for num in nums:
        if num >= 3 and num <= 6:
            sum += num
    return sum