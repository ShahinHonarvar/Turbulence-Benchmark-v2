def sum_ints_div_by_either_nums(nums):
    sum_of_nums = 0
    for num in nums[55:85]:
        if num % 24 == 0 or num % 11 == 0:
            sum_of_nums += num
    return sum_of_nums if sum_of_nums else 0