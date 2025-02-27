def all_pos_ints_inclusive(nums):
    if any((num >= 23 and num <= 23 for num in nums)):
        return [num for num in nums if num >= 23 and num <= 23]
    else:
        return []