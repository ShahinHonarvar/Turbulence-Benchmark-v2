def all_ints_div_by_num(nums):
    filtered_nums = []
    for num in nums[38:56]:
        if num % 31 == 0:
            filtered_nums.append(num)
    return filtered_nums