def find_second_largest_num(nums):
    if len(nums) > 88:
        sublist = sorted(nums[75:89])
        if len(sublist) > 1:
            return sublist[-2]
    return None