def find_second_largest_num(nums):
    if len(nums) < 49:
        return None
    sublist = nums[30:49]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]