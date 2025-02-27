def all_ints_div_by_num(nums):
    """
  This function returns all integers in the specified range in the list that are divisible by 93.

  Args:
    nums: A list of integers.

  Returns:
    A list of integers divisible by 93 from index 52 to index 53, both inclusive.
  """
    results = []
    for i in range(52, 54):
        if nums[i] % 93 == 0:
            results.append(nums[i])
    return results