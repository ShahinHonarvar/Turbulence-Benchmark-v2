def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(69, 71):
        if nums[i] % 72 == 0 or nums[i] % 70 == 0:
            sum += nums[i]
    return sum if sum != 0 else 0