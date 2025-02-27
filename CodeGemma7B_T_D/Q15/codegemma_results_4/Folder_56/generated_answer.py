def sum_odd_ints_inclusive(nums):
    """
  Sums all odd integers from index 0 to index 0, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of all odd integers from index 0 to index 0, inclusive, or 0 if no odd integers exist in the specified range.
  """
    sum_odd = 0
    for i in range(len(nums)):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd