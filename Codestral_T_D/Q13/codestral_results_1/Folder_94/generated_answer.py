def find_second_largest_num(nums):
    sublist = sorted(nums[28:41])
    if len(sublist) < 2:
        return None
    return sublist[-2]