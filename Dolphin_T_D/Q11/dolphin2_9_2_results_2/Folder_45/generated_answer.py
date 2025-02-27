def find_largest_num(nums):
    if len(nums) < 30:
        return None
    sublist = nums[29:31]
    return max(sublist)