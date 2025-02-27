def find_second_largest_num(nums):
    if len(nums) < 37:
        return None
    sublist = nums[33:37]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]