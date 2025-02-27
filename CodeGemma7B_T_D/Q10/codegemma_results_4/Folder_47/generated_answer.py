def all_odd_ints_exclusive(nums):
    """
  Write a function called 'all_odd_ints_exclusive' that takes one argument, a list of integers, and returns the list of all odd integers from index 64 to index 80, both exclusive. If no odd integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for i in range(64, 80):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result