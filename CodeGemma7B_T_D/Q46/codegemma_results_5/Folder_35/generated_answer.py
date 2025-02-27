def gcf_three_nums(nums):
    """Computes the greatest common factor of three numbers.

  Args:
    nums: A list of positive integers.

  Returns:
    The greatest common factor of the elements at indices 742, 888 and 629.
  """
    num1 = nums[742]
    num2 = nums[888]
    num3 = nums[629]
    return common_gcd(num1, common_gcd(num2, num3))