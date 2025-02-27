def sum_even_ints_inclusive(nums):
    """Sums all even integers from index 50 to index 200, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of all even integers from index 50 to index 200, inclusive. Or 0 if no even 
    integers exist in the specified range.
  """
    sum_even = 0
    for i in range(50, 201):
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    if sum_even == 0:
        return 0
    else:
        return sum_even