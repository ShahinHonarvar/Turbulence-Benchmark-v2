def sum_ints_div_by_either_nums(nums):
    sum_div = 0
    for i in range(31, 51):
        num = nums[i]
        if num % 81 == 0 or num % 64 == 0:
            sum_div += num
    return sum_div if sum_div else 0