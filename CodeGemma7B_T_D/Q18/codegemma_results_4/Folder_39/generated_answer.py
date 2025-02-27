def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for num in nums[13:77]:
        if num % -66 == 0 or num % -32 == 0:
            sum_nums += num
    return sum_nums if sum_nums else 0