def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums = sorted(nums[:10])
    return nums[-2] if len(nums) > 1 else None