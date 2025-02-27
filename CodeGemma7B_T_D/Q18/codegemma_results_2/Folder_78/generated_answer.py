def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[34:70]:
        if num % 19 == 0 or num % 32 == 0:
            result += num
    if result == 0:
        return 0
    return result