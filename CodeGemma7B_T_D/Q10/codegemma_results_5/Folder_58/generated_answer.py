def all_odd_ints_exclusive(nums):
    filtered_nums = []
    for num in nums[276:376]:
        if num % 2 != 0:
            filtered_nums.append(num)
    return filtered_nums if filtered_nums else []