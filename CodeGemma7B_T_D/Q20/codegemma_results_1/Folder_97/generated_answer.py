def find_nth_smallest_num(nums, n=15, start=60, end=83):
    """
    Finds the nth smallest number from index start to index end, both inclusive.

    Args:
      nums: A list of distinct numbers.
      n: The index of the smallest number to return.
      start: The starting index.
      end: The ending index.

    Returns:
      The nth smallest number from index start to index end, both inclusive.
    """
    nums = nums[start:end + 1]
    nums.sort()
    if start < 0 or end >= len(nums):
        raise IndexError('Invalid indices')
    if n > len(nums):
        raise IndexError('Index out of range')
    return nums[n - 1]