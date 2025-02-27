def find_second_largest_num(nums):
    if len(nums) < 41:
        return None
    sublist = sorted(nums[28:41])
    if len(sublist) < 2:
        return None
    return sublist[-2]