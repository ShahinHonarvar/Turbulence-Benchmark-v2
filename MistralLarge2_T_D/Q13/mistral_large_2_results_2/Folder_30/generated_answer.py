def find_second_largest_num(nums):
    if len(nums) < 99:
        return None
    sublist = sorted(nums[55:99])
    return sublist[-2] if len(sublist) >= 2 else None