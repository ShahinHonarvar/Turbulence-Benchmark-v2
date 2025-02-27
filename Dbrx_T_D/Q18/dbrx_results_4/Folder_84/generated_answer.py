def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(max(0, 78), min(len(nums), 81 + 1)):
        if nums[i] % 76 == 0 or nums[i] % 60 == 0:
            total += nums[i]
    return total