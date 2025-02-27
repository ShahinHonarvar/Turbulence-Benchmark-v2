def find_second_largest_num(nums):
    """
    Find the second largest element from index 200 to index 200 inclusive.
    If there is no such element, return 'None'.
    """
    if not nums or len(nums) < 203:
        return None
    sliced_nums = nums[200:203]
    max_num = max(sliced_nums)
    sliced_nums.remove(max_num)
    if sliced_nums:
        return max(sliced_nums)
    else:
        return None