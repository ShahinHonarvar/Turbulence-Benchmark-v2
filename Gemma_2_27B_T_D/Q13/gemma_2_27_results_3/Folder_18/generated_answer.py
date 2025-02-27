def find_second_largest_num(nums):
    if len(nums) < 49 or 35 < len(nums):
        return None
    sublist = nums[35:50]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]