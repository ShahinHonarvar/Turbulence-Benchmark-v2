def find_second_largest_num(nums):
    if len(nums) > 6:
        sublist = sorted(nums[6:7])
        if len(sublist) > 1:
            return sublist[-2]
    return None