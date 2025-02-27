def composite_nums_between_indices(list_of_nums):
    """
  Returns the set of composite numbers in the given list between index 31 to index 72, inclusive.

  Args:
    list_of_nums: A list of positive integers.

  Returns:
    The set of composite numbers in the given list between index 31 to index 72, inclusive. If no composite number exists in the specified range, an empty set is returned.
  """
    composite_nums = set()
    for i in range(31, 73):
        if list_of_nums[i] % 2 != 0 and list_of_nums[i] % 3 != 0 and (list_of_nums[i] % 5 != 0) and (list_of_nums[i] % 7 != 0):
            composite_nums.add(list_of_nums[i])
    return composite_nums