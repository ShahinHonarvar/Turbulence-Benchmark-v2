def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(61, 89):
        if i in range(len(nums)):
            if nums[i] % 31 == 0 or nums[i] % 11 == 0:
                sum += nums[i]
    return sum