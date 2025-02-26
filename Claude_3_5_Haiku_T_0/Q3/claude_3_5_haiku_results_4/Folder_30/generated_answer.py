def all_pos_ints_inclusive(nums):
    if len(nums) <= 55:
        return []
    end_index = min(98, len(nums) - 1)
    positive_ints = [num for num in nums[55:end_index + 1] if num > 0]
    return positive_ints