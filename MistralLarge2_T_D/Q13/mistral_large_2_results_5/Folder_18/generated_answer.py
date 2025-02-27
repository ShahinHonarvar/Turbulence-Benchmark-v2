def find_second_largest_num(nums):
    if len(nums) < 50:
        return None
    sublist = nums[35:50]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]