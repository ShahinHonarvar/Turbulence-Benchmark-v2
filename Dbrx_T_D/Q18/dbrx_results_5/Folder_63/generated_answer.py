def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(len(nums)):
        if i >= 31 and i <= 50:
            if nums[i] % 81 == 0 or nums[i] % 64 == 0:
                total += nums[i]
    return total