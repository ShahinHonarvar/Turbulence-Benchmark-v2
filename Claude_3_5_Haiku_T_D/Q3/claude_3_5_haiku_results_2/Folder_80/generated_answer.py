def all_pos_ints_inclusive(nums):
    if len(nums) < 67:
        return []
    result = [num for num in nums[64:67] if num > 0]
    return result