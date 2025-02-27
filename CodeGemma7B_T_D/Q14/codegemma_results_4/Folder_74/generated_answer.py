def find_second_smallest_num(nums):
    """
  Searches a list of numbers for the second smallest element, between indices 36 and 46, inclusive.
  Returns 'None' if no element is found within that range.
  """
    nums = [num for num in nums if 36 <= nums.index(num) <= 46]
    nums.sort()
    if len(nums) > 1:
        return nums[1]
    else:
        return None