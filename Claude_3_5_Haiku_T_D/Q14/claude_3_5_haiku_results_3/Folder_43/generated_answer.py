def find_second_smallest_num(nums):
    if len(nums) < 96 or len(nums) == 0:
        return None
    sublist = nums[74:96]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(set(sublist))
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]