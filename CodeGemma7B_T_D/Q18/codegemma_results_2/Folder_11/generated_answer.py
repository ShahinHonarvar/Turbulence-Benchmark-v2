def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[22:25]:
        if num % -85 == 0 or num % -30 == 0:
            sum += num
    return sum