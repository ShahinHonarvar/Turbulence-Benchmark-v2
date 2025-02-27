def find_second_smallest_num(nums):
    if len(nums) < 99:
        return None
    sublist = sorted(nums[56:99])
    return sublist[1] if len(sublist) > 1 else None