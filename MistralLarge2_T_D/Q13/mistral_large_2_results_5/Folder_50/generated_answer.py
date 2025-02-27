def find_second_largest_num(nums):
    if len(nums) < 71:
        return None
    sublist = nums[70:85]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None