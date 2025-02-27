def all_ints_not_div_by_num(nums):
    filtered_nums = [num for num in nums[30:200] if num % -115 != 0]
    return filtered_nums