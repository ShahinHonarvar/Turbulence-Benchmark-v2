def all_neg_ints_inclusive(nums):
    return [num for num in nums if num < 0 and nums.index(num) in range(34, 56)]