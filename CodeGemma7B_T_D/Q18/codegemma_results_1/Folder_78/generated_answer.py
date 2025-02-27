def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for num in nums[34:70]:
        if num % 19 == 0 or num % 32 == 0:
            total_sum += num
    return total_sum or 0