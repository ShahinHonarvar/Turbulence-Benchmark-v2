def all_pos_ints_exclusive(nums):
    if len(nums) <= 101:
        return []
    start_index = 101
    end_index = min(len(nums), 200)
    return [num for num in nums[start_index:end_index] if num > 0]