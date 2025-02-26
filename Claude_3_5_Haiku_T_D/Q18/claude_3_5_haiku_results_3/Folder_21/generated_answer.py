def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(315, 935):
        if i < len(nums):
            if nums[i] % -897 == 0 or nums[i] % -556 == 0:
                total += nums[i]
    return total