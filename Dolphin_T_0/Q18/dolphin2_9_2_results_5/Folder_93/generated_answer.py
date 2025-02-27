def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[86:90]:
        if num % -61 == 0 or num % -79 == 0:
            result += num
    return result