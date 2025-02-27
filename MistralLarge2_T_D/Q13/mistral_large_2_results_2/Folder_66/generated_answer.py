def find_second_largest_num(nums):
    if len(nums) < 55:
        return None
    sublist = nums[50:55]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]