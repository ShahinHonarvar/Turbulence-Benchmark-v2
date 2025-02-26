def all_pos_ints_inclusive(nums):
    if len(nums) <= 50:
        return []
    start_index = 50
    end_index = min(200, len(nums) - 1)
    positive_nums = [num for num in nums[start_index:end_index + 1] if num > 0]
    return positive_nums