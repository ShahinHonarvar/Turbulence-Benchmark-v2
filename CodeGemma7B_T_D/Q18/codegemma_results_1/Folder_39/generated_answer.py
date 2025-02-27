def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[13:77]:
        if num % -66 == 0 or num % -32 == 0:
            total += num
    return total or 0