def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(69, 98):
        if i < len(nums):
            if nums[i] % -90 == 0 or nums[i] % -67 == 0:
                total += nums[i]
    return total