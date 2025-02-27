def all_ints_not_div_by_num(nums):
    filtered_nums = []
    for num in nums[0:5]:
        if num % 8 != 0:
            filtered_nums.append(num)
    return filtered_nums