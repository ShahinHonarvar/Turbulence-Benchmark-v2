def all_neg_ints_inclusive(nums):
    result = [num for num in nums[10:101] if num < 0]
    return result if result else []