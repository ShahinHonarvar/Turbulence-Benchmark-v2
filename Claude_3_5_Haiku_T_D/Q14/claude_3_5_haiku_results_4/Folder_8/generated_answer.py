def find_second_smallest_num(nums):
    if len(nums) < 58:
        return None
    sublist = nums[56:67]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(set(sublist))
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]