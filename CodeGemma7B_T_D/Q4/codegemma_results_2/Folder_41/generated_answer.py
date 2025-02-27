def all_pos_ints_exclusive(nums):
    """
  Returns all positive integers from index 8 to index 9, both exclusive, in a list.

  Args:
    nums: A list of integers.

  Returns:
    A list of positive integers from index 8 to index 9, both exclusive. If no
    positive integers exist in the specified range, returns an empty list.
  """
    positive_ints = []
    for num in nums:
        if num > 0 and 8 < nums.index(num) < 9:
            positive_ints.append(num)
    return positive_ints