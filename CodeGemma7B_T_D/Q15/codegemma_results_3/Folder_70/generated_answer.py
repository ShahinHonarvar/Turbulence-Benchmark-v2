def sum_odd_ints_inclusive(nums):
    """
  Sums the odd integers from index 28 to index 32, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    The sum of all odd integers from index 28 to index 32, inclusive. If no such integers exist, returns 0.
  """
    has_odd_integers = any((num % 2 == 1 for num in nums[28:33]))
    return sum((num for num in nums[28:33] if num % 2 == 1), 0) if has_odd_integers else 0