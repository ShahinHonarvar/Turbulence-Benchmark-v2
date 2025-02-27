def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[38:82]:
        if num % -61 == 0 or num % -71 == 0:
            total += num
    return total or 0