def sum_in_range(nums):
    """Sums all numbers in the list nums that are between 6 and 8, both inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of all numbers in the list nums that are between 6 and 8, both inclusive. If the given list does not contain such integers, the function should return 0.
  """
    sum = 0
    for i in nums:
        if i >= 6 and i <= 8:
            sum += i
    return sum