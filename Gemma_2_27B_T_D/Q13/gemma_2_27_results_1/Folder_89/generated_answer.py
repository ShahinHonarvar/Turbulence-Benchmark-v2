def find_second_largest_num(nums):
    if len(nums) < 82 - 56 + 1:
        return None
    sublist = nums[56:83]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[-2]