def find_second_largest_num(nums):
    if len(nums) < 46:
        return None
    sublist = nums[36:47]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]