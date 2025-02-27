def find_second_largest_num(nums):
    if len(nums) < 22:
        return None
    sublist = nums[34:56]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[-2]