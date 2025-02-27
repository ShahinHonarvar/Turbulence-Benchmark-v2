def find_second_largest_num(nums):
    sublist = nums[29:94]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[-2]