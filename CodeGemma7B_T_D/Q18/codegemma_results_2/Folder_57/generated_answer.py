def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[51:77]:
        if num % -90 == 0 or num % -59 == 0:
            total += num
    return total or 0