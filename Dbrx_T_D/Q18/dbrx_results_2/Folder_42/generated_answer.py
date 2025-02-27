def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(29, 46):
        num = nums[i]
        if num % 27 == 0 or num % 81 == 0:
            total += num
    return total