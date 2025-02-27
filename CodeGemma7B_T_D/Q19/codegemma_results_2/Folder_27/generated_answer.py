def all_ints_not_div_by_num(nums):
    filtered_nums = []
    for num in nums[14:21]:
        if num % -93 != 0:
            filtered_nums.append(num)
    return filtered_nums