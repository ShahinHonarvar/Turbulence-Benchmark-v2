def find_second_smallest_num(nums):
    if 52 <= len(nums) <= 71:
        sublist = sorted(nums[52:72])
        return sublist[1] if len(sublist) > 1 else None
    return None