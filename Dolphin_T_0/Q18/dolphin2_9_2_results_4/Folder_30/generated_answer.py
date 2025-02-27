def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[10:76]:
        if num % -81 == 0 or num % -94 == 0:
            result += num
    return result