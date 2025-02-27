def all_neg_ints_inclusive(nums):
    nums = nums[62:79]
    nums = [num for num in nums if num < 0]
    return nums if nums else []