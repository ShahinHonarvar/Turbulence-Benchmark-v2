def all_ints_not_div_by_num(nums):
    filtered_nums = [num for num in nums[41:69] if num % -82 != 0]
    return filtered_nums if filtered_nums else []