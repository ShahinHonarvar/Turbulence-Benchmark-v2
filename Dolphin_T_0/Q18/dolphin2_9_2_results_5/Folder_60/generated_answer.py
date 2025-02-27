def sum_ints_div_by_either_nums(nums):
    sum_ = 0
    for num in nums[10:80]:
        if num % -74 == 0 or num % -58 == 0:
            sum_ += num
    return sum_