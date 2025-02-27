def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for num in nums[61:89]:
        if num % 31 == 0 or num % 11 == 0:
            sum_nums += num
    return sum_nums