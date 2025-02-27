def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[57:82]:
        if num % 55 == 0 or num % 10 == 0:
            total += num
    return total