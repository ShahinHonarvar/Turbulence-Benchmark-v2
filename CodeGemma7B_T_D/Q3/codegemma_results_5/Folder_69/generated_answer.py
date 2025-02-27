def all_pos_ints_inclusive(nums):
    if not any((num > 0 for num in nums[32:36])):
        return []
    return [num for num in nums[32:36] if num > 0]