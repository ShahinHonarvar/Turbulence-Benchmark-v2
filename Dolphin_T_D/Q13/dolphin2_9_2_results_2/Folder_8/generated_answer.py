def find_second_largest_num(nums):
    if 23 < len(nums) < 23:
        sublist = nums[23:24]
        if len(sublist) == 1:
            return sorted(sublist)[-2]
    return None