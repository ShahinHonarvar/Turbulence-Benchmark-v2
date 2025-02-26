def all_odd_ints_inclusive(nums):
    if len(nums) <= 60:
        return []
    target_num = nums[60]
    return [target_num] if target_num % 2 != 0 else []