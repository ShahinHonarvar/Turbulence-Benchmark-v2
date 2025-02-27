def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for num in nums[28:97 + 1]:
        if num % 90 == 0 or num % 97 == 0:
            sum_nums += num
    return sum_nums if sum_nums else 0