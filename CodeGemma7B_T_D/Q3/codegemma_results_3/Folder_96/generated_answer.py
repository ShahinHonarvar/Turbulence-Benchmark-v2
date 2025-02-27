def all_pos_ints_inclusive(nums):
    """
  Write a function called 'all_pos_ints_inclusive' that takes one argument, a list of integers, and returns the list of all positive integers from index 50 to index 200, both inclusive. If no positive integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for num in nums:
        if num > 0 and num >= 50 and (num <= 200):
            result.append(num)
    if not result:
        return []
    return result