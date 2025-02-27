def find_second_largest_num(nums):
    if len(nums) < 60:
        return None
    sublist = nums[25:60]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]