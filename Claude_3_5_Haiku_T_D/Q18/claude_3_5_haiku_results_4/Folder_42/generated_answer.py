def sum_ints_div_by_either_nums(nums):
    if len(nums) < 46:
        return 0
    total = 0
    for num in nums[29:46]:
        if num % 27 == 0 or num % 81 == 0:
            total += num
    return total