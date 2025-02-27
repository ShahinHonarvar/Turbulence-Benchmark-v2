def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for num in nums[55:85]:
        if num % -24 == 0 or num % -11 == 0:
            total_sum += num
    return total_sum