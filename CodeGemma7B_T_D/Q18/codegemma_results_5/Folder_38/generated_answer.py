def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for num in nums[10:77]:
        if num % 40 == 0 or num % 12 == 0:
            total_sum += num
    if total_sum == 0:
        return 0
    return total_sum