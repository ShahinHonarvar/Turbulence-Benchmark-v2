def all_pos_ints_inclusive(nums):
    if len(nums) <= 26:
        return []
    end_index = min(52, len(nums) - 1)
    return [num for num in nums[26:end_index + 1] if num > 0]