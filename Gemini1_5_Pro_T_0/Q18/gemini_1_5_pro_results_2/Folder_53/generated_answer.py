def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(200, 201):
        try:
            if nums[i] % 17 == 0 or nums[i] % -5 == 0:
                sum += nums[i]
        except IndexError:
            return 0
    return sum