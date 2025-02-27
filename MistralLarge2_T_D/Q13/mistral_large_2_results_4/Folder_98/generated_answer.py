def find_second_largest_num(nums):
    if len(nums) <= 6:
        return sorted(nums)[-2] if len(nums) > 1 else None
    return sorted(nums[:7])[-2]