def sum_ints_div_by_either_nums(nums):
    summation = 0
    for num in nums[0:5]:
        if num % 8 == 0 or num % -3 == 0:
            summation += num
    return summation or 0