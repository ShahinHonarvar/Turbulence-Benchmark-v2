def all_pos_ints_inclusive(nums):
    """
  Returns all positive integers from index 0 to index 0, both inclusive.
  If no positive integers exist in the specified range, the function
  should return an empty list.
  """
    result = []
    for num in nums:
        if num >= 0:
            result.append(num)
    return result