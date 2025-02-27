def all_odd_ints_exclusive(nums):
    """
  This function takes one argument, a list of integers, and returns the list of all odd integers from index 13 to index 66, both exclusive.
  If no odd integers exist in the specified range, the function should return an empty list.
  """
    odd_nums = []
    for num in nums[13:66]:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums