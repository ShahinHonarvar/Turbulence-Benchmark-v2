def all_even_ints_inclusive(nums):
    """
  Returns a list of all even integers from index 0 to index 4, both inclusive.
  If no even integers exist in the specified range, the function should return an empty list.
  """
    even_nums = []
    for i in range(5):
        if i >= 0 and i <= 4 and (nums[i] % 2 == 0):
            even_nums.append(nums[i])
    return even_nums