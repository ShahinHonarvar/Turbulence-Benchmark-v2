def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(len(nums)):
        if i >= 10 and i <= 100 and (nums[i] % 10 == 0 or nums[i] % 100 == 0):
            total += nums[i]
    return total if total > 0 else 0