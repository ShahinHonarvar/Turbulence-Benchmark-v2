def all_neg_ints_inclusive(nums):
    return [num for num in nums if num <= 0 and num >= -8 and (nums.index(num) in range(1, 9))]