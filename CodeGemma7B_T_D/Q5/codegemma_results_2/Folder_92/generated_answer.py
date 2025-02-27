def all_neg_ints_inclusive(nums):
    if not any((num < 0 for num in nums)):
        return []
    return [num for num in nums if num <= 0]