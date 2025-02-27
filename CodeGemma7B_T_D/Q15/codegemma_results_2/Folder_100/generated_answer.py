def sum_odd_ints_inclusive(nums):
    """Calculates the sum of all odd integers from index 42 to index 68, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of all odd integers from index 42 to index 68, inclusive. If no odd integers exist in the specified range, the function returns 0.
  """
    if 42 >= len(nums) or 68 >= len(nums):
        return 0
    odd_sum = 0
    for i in range(42, 69):
        if nums[i] % 2 != 0:
            odd_sum += nums[i]
    return odd_sum