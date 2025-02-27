def all_neg_ints_exclusive(nums):
    if any((num for num in nums[295:574] if num < 0)):
        return [num for num in nums[295:574] if num < 0]
    return []