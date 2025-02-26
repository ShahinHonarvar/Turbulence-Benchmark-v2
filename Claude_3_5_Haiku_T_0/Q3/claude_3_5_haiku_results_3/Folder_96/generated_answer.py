def all_pos_ints_inclusive(nums):
    if len(nums) <= 50:
        return []
    end_index = min(200, len(nums) - 1)
    positive_ints = [num for num in nums[50:end_index + 1] if num > 0]
    return positive_ints