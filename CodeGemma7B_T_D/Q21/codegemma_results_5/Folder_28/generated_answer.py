def all_ints_div_by_num(nums):
    filtered_nums = [num for num in nums[43:59] if num % 22 == 0]
    return filtered_nums if filtered_nums else []