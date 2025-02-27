def sum_ints_div_by_either_nums(nums):
    sum_int = 0
    for i in range(13, 19):
        num = nums[i]
        if num % 45 == 0 or num % 20 == 0:
            sum_int += num
    if sum_int == 0:
        return 0
    else:
        return sum_int