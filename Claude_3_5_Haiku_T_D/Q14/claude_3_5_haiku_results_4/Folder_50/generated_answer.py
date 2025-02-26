def find_second_smallest_num(nums):
    if len(nums) < 43:
        return None
    sublist = nums[42:69]
    if not sublist:
        return None
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None