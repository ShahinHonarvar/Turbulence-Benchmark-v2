def all_ints_div_by_both_two_nums(nums):
    """
  Returns all integers in a list divisible by both -20 and -200 from index 20 to index 200, both inclusive.
  If no such integers exist, the function returns an empty list.
  """
    if not nums:
        return []
    result = []
    for i in range(20, 201):
        if i % -20 == 0 and i % -200 == 0:
            result.append(i)
    return result