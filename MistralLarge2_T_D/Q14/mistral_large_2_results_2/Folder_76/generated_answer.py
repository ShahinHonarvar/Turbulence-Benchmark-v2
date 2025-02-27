def find_second_smallest_num(nums):
    sublist = nums[533:606]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist))
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]