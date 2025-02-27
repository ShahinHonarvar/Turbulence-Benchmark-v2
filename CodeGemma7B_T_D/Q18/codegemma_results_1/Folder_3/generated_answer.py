def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[38:53]:
        if num % -41 == 0 or num % -47 == 0:
            result += num
    return result