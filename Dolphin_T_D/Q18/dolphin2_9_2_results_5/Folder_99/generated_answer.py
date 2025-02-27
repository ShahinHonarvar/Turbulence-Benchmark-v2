def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[798:154:-1]:
        if num % 275 == 0 or num % 580 == 0:
            total += num
    return total