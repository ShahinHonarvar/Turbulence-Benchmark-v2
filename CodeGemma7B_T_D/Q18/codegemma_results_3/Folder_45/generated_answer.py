def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for num in nums[30:201]:
        if num % -115 == 0 or num % 115 == 0:
            sum_nums += num
    return sum_nums