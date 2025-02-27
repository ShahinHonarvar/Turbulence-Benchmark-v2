def find_n_th_smallest_num(nums):
    """
    Finds the seventh smallest number from index 85 to index 99, inclusive.

    Args:
      nums: A list of distinct numbers.

    Returns:
      The seventh smallest number.
  """
    nums_sorted = sorted(nums)
    return nums_sorted[84:100][6]