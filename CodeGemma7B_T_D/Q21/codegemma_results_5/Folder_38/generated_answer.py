def all_ints_div_by_num(nums):
    filtered_nums = []
    for num in nums[12:16]:
        if num % -80 == 0:
            filtered_nums.append(num)
    return filtered_nums