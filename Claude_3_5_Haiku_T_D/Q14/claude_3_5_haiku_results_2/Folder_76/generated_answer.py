def find_second_smallest_num(nums):
    if len(nums) <= 533:
        return None
    sublist = nums[533:606]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None