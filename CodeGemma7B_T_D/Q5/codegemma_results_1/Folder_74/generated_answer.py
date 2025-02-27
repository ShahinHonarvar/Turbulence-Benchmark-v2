def all_neg_ints_inclusive(nums):
    filtered_nums = [num for num in nums[17:79] if num < 0]
    return filtered_nums if filtered_nums else []