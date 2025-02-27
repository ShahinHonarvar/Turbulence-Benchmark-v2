def find_second_largest_num(nums):
    if len(nums) < 56:
        return None
    sublist = nums[34:56]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]