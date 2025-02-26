def all_pos_ints_inclusive(nums):
    if len(nums) <= 56:
        return []
    end_index = min(98, len(nums) - 1)
    return [num for num in nums[56:end_index + 1] if num > 0]