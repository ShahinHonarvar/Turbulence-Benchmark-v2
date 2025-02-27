def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    sublist = nums[62:64]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]