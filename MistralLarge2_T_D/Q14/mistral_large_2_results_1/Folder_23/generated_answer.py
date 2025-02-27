def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    sublist = sorted(nums[19:93])
    return sublist[1] if len(sublist) > 1 else None