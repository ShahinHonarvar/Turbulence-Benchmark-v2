def all_neg_ints_exclusive(nums):
    return [] if all((num >= 0 for num in nums[1:3])) else [num for num in nums if num < 0 and 0 < nums.index(num) < 3]