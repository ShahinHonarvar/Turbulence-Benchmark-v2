def find_second_largest_num(nums):
    if len(nums) < 67:
        return None
    sublist = sorted(nums[56:67])
    if len(sublist) < 2:
        return None
    return sublist[-2]