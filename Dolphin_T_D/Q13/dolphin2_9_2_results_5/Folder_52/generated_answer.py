def find_second_largest_num(nums):
    if 28 <= 38 < len(nums):
        sublist = nums[28:39]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[-2]
    return None