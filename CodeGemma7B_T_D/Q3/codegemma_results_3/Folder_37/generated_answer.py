def all_pos_ints_inclusive(nums):
    if not any((num > 0 and i + 1 >= 1 and (i + 1 <= 5) for i, num in enumerate(nums))):
        return []
    return [num for num in nums if num > 0 and (num >= 1 and num <= 5)]