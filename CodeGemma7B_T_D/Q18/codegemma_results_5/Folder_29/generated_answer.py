def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[55:85]:
        if num % -24 == 0 or num % -11 == 0:
            result += num
    if result == 0:
        return 0
    else:
        return result