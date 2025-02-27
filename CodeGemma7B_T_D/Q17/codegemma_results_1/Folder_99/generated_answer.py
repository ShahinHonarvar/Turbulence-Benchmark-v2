def all_ints_div_by_both_two_nums(nums):
    filtered_nums = []
    for num in nums[154:800]:
        if num % 275 == 0 and num % 580 == 0:
            filtered_nums.append(num)
    return filtered_nums