def all_neg_ints_exclusive(nums):
    filtered_nums = [num for num in nums[276:376] if num < 0]
    return filtered_nums if filtered_nums else []