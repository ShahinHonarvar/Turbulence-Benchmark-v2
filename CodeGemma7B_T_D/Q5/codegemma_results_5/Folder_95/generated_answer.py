def all_neg_ints_inclusive(nums):
    return [num for num in nums if num <= 0 and num >= -86 and (nums.index(num) in range(82, 87))]