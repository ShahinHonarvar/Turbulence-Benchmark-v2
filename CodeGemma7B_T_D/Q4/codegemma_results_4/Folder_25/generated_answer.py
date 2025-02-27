def all_pos_ints_exclusive(nums):
    """
  Returns the list of all positive integers from index 41 to index 69, both exclusive.

  Args:
    nums: A list of integers.

  Returns:
    A list of positive integers from index 41 to index 69, both exclusive. If no positive integers exist in the specified range, an empty list is returned.
  """
    pos_ints = []
    for num in nums:
        if num > 0 and 41 < nums.index(num) < 69:
            pos_ints.append(num)
    return pos_ints