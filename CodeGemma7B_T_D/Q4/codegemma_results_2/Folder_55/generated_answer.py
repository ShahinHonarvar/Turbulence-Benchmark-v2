def all_pos_ints_exclusive(nums):
    """
  Returns the list of all positive integers from index 0 to index 10, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for i in range(1, 11):
        if i in nums:
            result.append(i)
    return result