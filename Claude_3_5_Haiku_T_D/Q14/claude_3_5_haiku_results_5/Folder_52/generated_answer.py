def find_second_smallest_num(nums):
    if len(nums) < 67:
        return None
    sublist = nums[64:67]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None