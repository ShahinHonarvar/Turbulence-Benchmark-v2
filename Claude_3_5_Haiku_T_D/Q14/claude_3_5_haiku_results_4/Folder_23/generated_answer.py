def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    sublist = nums[19:93]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(set(sublist))
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]