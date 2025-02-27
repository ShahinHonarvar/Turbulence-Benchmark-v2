def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[50:93]:
        if num % -94 == 0 or num % -95 == 0:
            result += num
    return result if result else 0