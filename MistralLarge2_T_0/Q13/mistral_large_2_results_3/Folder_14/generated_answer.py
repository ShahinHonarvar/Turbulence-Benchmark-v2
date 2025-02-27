def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    sublist = nums[5:8]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]