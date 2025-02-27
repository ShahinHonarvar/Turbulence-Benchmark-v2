def all_ints_div_by_num(nums):
    """
  This function takes a list of integers and returns the list of all integers
  divisible by -12 from index 10 to index 52, both inclusive. If no such
  integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for i in range(10, 53):
        if nums[i] % -12 == 0:
            result.append(nums[i])
    return result