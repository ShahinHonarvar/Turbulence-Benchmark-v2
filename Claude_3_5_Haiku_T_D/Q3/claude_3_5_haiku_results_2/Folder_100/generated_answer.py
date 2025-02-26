def all_pos_ints_inclusive(nums):
    if len(nums) < 69:
        return []
    result = [num for num in nums[42:69] if num > 0]
    return result