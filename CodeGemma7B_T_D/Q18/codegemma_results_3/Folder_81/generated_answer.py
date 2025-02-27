def sum_ints_div_by_either_nums(nums):
    sum_num = 0
    for num in nums[10:101]:
        if num % 10 == 0 or num % 100 == 0:
            sum_num += num
    return sum_num