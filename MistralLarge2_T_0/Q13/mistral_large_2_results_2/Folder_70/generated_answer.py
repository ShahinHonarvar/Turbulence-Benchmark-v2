def find_second_largest_num(nums):
    if len(nums) < 33:
        return None
    sublist = nums[28:33]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]