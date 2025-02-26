def all_pos_ints_inclusive(nums):
    if len(nums) <= 25:
        return []
    end_index = min(87, len(nums) - 1)
    positive_ints = [num for num in nums[25:end_index + 1] if num > 0]
    return positive_ints