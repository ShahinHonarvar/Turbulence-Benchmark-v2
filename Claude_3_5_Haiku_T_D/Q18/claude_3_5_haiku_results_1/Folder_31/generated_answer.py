def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(56, 89):
        if i < len(nums):
            if nums[i] % -59 == 0 or nums[i] % -79 == 0:
                total += nums[i]
    return total