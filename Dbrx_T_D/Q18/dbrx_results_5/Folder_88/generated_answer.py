def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(len(nums)):
        if 3 <= i <= 9:
            if nums[i] % 6 == 0 or nums[i] % 1 == 0:
                total += nums[i]
    return total