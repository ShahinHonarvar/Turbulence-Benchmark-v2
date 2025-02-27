def sum_even_ints_inclusive(nums):
    """
  Sums all even integers from index 661 to 924, inclusive. If no even integers exist in the specified range, returns 0.
  """
    sum_even = 0
    for i in range(661, 925):
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    if sum_even == 0:
        return 0
    else:
        return sum_even