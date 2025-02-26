def all_odd_ints_inclusive(nums):
    if len(nums) <= 60:
        return []
    target_number = nums[60]
    return [target_number] if target_number % 2 != 0 else []