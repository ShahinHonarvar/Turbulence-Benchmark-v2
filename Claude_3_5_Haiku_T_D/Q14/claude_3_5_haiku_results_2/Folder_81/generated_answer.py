def find_second_smallest_num(nums):
    if len(nums) < 102:
        return None
    sublist = nums[10:101]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist))
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]