def all_neg_ints_inclusive(nums):
    if not any((num < 0 for num in nums)):
        return []
    neg_nums = [num for num in nums[80:201] if num < 0]
    return neg_nums