def find_second_smallest_num(nums):
    sublist = nums[13:69]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]