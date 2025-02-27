def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[37:53]:
        if num % -41 == 0 or num % -47 == 0:
            total += num
    return total