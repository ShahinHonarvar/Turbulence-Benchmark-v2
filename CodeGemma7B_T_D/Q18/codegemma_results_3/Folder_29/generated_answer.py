def sum_ints_div_by_either_nums(nums):
    sum_ = 0
    for i in range(55, 85):
        if nums[i] % 24 == 0 or nums[i] % 11 == 0:
            sum_ += nums[i]
    return sum_ if sum_ else 0