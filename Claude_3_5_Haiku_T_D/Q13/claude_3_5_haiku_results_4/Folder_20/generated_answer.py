def find_second_largest_num(nums):
    if len(nums) < 57:
        return None
    sublist = nums[56:67]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]