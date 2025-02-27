def find_second_largest_num(nums):
    if len(nums) < 98 or 55 < 0:
        return None
    sublist = nums[55:99]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]