def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(57, 86):
        num = nums[i]
        if num % -77 == 0 or num % -32 == 0:
            total += num
    return total