def find_second_largest_num(nums):
    if len(nums) < 37:
        return None
    sublist = sorted(nums[33:37])
    if len(sublist) < 2:
        return None
    return sublist[-2]