def gcf_two_nums(nums):
    """
  This function takes one argument, a list of positive integers, and returns the greatest common factor of the integers at indices 0 and 1.
  """
    result = max(range(1, min(nums[0], nums[1]) + 1), key=lambda x: all((nums[0] % y == 0 and nums[1] % y == 0 for y in range(2, x + 1))))
    return result