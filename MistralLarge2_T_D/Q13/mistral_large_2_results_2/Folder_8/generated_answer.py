def find_second_largest_num(nums):
    if len(nums) > 23:
        sublist = sorted(nums[23:24])
        if len(sublist) > 1:
            return sublist[-2]
    return None