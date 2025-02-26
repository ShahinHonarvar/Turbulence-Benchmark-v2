def find_second_largest_num(nums):
    if len(nums) < 22:
        return None
    sublist = nums[20:31]
    if len(sublist) < 2:
        return None
    unique_sublist = sorted(set(sublist), reverse=True)
    return unique_sublist[1] if len(unique_sublist) >= 2 else None