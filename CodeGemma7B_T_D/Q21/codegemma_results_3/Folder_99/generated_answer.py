def all_ints_div_by_num(nums):
    """
  Returns a list of all integers in the list divisible by 763 from index 161 to index 970, inclusive.
  If no such integers exist in the specified range, the function returns an empty list.
  """
    res = []
    for num in nums[161:971]:
        if num % 763 == 0:
            res.append(num)
    return res