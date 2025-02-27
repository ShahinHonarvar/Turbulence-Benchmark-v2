def find_second_largest_num(nums):
    if len(nums) < 96:
        return None
    sublist = sorted(nums[74:96])
    if len(sublist) < 2:
        return None
    return sublist[-2]