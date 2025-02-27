def sum_even_ints_inclusive(nums):
    """
  Sums even numbers from index 5 to index 7, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of even integers from index 5 to index 7, inclusive. If no even
    integers exist in the specified range, returns 0.
  """
    num_sum = 0
    for i in range(5, 8):
        if nums[i] % 2 == 0:
            num_sum += nums[i]
    if num_sum == 0:
        return 0
    return num_sum