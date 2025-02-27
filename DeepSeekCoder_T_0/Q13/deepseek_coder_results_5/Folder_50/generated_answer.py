def find_second_largest_num(nums):
    if len(nums) < 85:
        return None
    sublist = sorted(nums[70:85])
    if len(sublist) < 2:
        return None
    return sublist[-2]