def find_second_largest_num(nums):
    if 36 < len(nums):
        sublist = nums[33:37]
        if len(set(sublist)) > 1:
            sublist.sort()
            return sublist[-2]
    return None