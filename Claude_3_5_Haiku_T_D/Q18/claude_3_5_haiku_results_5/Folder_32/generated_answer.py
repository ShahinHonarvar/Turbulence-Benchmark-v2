def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[25:96]:
        if num % 51 == 0 or num % 77 == 0:
            total += num
    return total