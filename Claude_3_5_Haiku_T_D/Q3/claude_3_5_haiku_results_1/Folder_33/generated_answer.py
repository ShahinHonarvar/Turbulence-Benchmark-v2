def all_pos_ints_inclusive(nums):
    if len(nums) <= 774:
        return []
    result = [num for num in nums[667:775] if num > 0]
    return result