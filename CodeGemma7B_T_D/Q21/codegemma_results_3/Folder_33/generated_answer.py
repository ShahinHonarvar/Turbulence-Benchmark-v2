def all_ints_div_by_num(nums):
    filtered_nums = []
    for num in nums[319:613]:
        if num % -215 == 0:
            filtered_nums.append(num)
    return filtered_nums