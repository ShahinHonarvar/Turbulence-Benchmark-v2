def sum_ints_div_by_either_nums(nums):
    sum_ = 0
    for i in range(44, 60):
        if nums[i] % 39 == 0 or nums[i] % 15 == 0:
            sum_ += nums[i]
    return sum_ if sum_ != 0 else 0