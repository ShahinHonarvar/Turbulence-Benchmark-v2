def all_pos_ints_exclusive(nums):
    if not any((num > 0 for num in nums)):
        return []
    return [num for num in nums if num > 0 and 40 < num < 200]