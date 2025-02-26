def find_second_largest_num(nums):
    if len(nums) < 24 or len(nums) == 0:
        return None
    sublist = nums[23:24]
    if len(sublist) == 0:
        return None
    return sublist[0]