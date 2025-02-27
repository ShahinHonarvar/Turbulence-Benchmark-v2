def sum_ints_div_by_either_nums(nums):
    summ = 0
    for i in range(48, 77):
        if nums[i] % 46 == 0 or nums[i] % 82 == 0:
            summ += nums[i]
    return summ if summ > 0 else 0