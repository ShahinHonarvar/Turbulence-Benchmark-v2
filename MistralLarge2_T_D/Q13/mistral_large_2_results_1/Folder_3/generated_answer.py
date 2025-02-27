def find_second_largest_num(nums):
    if len(nums) > 92:
        sublist = nums[62:93]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[-2]
    return None