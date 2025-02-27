def sum_in_range(nums):
    """
  This function takes one argument, a list of integers, and returns the sum of all integers from the given list that are between -3 and 6, both inclusive. If the given list does not contain such integers, the function should return 0.
  """
    sum = 0
    for num in nums:
        if num >= -3 and num <= 6:
            sum += num
    return sum