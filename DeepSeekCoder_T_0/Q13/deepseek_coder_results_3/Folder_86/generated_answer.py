def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    sublist = sorted(nums[31:35])
    if len(sublist) < 2:
        return None
    return sublist[-2]