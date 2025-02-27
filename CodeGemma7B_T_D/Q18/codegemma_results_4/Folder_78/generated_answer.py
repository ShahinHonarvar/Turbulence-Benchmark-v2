def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in nums[34:70]:
        if i % 19 == 0 or i % 32 == 0:
            total += i
    return total or 0