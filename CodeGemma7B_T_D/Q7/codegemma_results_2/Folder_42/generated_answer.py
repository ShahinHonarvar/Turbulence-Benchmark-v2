def all_even_ints_inclusive(nums):
    """
  Returns a list of all even integers from index 29 to index 79, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    A list of even integers from index 29 to index 79, inclusive. If no even integers exist in the specified range, an empty list is returned.
  """
    if not nums:
        return []
    if len(nums) < 29:
        return []
    even_ints = []
    for i in range(29, 80):
        if nums[i] % 2 == 0:
            even_ints.append(nums[i])
    return even_ints