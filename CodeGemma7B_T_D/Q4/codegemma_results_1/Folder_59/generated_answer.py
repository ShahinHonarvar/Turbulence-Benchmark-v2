def all_pos_ints_exclusive(nums):
    """
  Returns the list of all positive integers from index 0 to index 9, both exclusive.
  If no positive integers exist in the specified range, the function should return an empty list.
  """
    pos_ints = []
    for num in nums:
        if num > 0 and num <= 9:
            pos_ints.append(num)
    return pos_ints