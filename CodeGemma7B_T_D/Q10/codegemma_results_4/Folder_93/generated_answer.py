def all_odd_ints_exclusive(nums):
    filtered_nums = [num for num in nums[19:95] if num % 2 != 0]
    return filtered_nums if filtered_nums else []