def all_pos_ints_inclusive(nums):
    if len(nums) < 9:
        return []
    return [num for num in nums[1:9] if num > 0]