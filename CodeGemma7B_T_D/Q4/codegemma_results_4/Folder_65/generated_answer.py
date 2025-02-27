def all_pos_ints_exclusive(nums):
    if not any((num > 0 for num in nums[42:88])):
        return []
    return [num for num in nums[42:88] if num > 0]