def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[306:958]:
        if num % 982 == 0 or num % 319 == 0:
            total += num
    return total