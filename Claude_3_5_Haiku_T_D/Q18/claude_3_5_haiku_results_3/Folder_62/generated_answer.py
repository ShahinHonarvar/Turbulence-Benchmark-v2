def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[44:60]:
        if num % 39 == 0 or num % 15 == 0:
            total += num
    return total