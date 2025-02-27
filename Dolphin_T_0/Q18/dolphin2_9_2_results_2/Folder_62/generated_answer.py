def sum_ints_div_by_either_nums(nums):
    sum_ = 0
    for num in nums[44:60]:
        if num % 39 == 0 or num % 15 == 0:
            sum_ += num
    return sum_