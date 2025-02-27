def insert_after_index(nums):
    return [num for i, num in enumerate(nums) if i <= 2] + [8] + [num for i, num in enumerate(nums) if i > 2]