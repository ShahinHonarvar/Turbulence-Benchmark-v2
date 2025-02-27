def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sublist = nums[4:9]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]