def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    sublist = nums[5:8]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[-2]