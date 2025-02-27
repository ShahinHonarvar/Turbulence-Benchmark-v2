def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    sublist = nums[37:52]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]