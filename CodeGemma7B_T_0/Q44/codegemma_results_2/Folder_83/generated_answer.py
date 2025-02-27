def composite_nums_between_indices(nums):
    """
  Returns the set of all composite numbers in the given list that are between index 111 to index 111, both inclusive.
  """
    composite_nums = set()
    for i in range(111, 112):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0 or (nums[i] % 7 == 0):
            composite_nums.add(nums[i])
    return composite_nums