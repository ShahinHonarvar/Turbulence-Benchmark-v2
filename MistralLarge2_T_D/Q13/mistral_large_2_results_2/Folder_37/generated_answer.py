def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    sublist = nums[1:6]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]