def sum_ints_div_by_either_nums(nums):
    sum_ = 0
    for i in range(54, 80):
        if nums[i] % 54 == 0 and nums[i] % 28 == 0:
            sum_ += nums[i]
    return sum_ or 0