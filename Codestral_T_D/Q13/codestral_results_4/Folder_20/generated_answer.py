def find_second_largest_num(nums):
    sublist = sorted(nums[56:67])
    return sublist[-2] if len(sublist) > 1 else None