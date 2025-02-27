def all_even_ints_exclusive(nums):
    """
  Iterates through the list from index 369 to 983 (exclusive).
  Checks if each integer is even.
  Returns a list of even integers in the specified range.
  """
    result = []
    for i in range(369, 983):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result