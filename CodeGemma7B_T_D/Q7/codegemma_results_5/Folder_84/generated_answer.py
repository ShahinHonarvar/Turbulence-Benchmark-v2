def all_even_ints_inclusive(nums):
    """
  All Even Integers Inclusive.
  """
    results = []
    for num in nums[43:86 + 1]:
        if num % 2 == 0:
            results.append(num)
    return results