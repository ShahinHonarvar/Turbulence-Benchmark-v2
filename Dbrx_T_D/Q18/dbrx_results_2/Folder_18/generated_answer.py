def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(len(nums)):
        if i >= 55 and i <= 66:
            if nums[i] % 22 == 0 or nums[i] % 82 == 0:
                total += nums[i]
    return total