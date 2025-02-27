def all_odd_ints_exclusive(nums):
    """
  This function takes a list of integers and returns the list of all odd integers from index 111 to index 473, both exclusive.
  If no odd integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for i in range(111, 473):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result