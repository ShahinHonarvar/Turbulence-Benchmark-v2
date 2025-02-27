def all_ints_div_by_both_two_nums(nums):
    filtered_nums = []
    for num in nums[48:77]:
        if num % -46 == 0 and num % -82 == 0:
            filtered_nums.append(num)
    return filtered_nums