def all_even_ints_inclusive(nums):
    """
  Return all even integers from index 21 to index 97, inclusive.
  """
    try:
        return [num for num in nums[21:98] if num % 2 == 0]
    except IndexError:
        return []