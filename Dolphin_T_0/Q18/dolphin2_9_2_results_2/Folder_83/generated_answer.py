def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[89:200]:
        if num % -31 == 0 or num % 13 == 0:
            result += num
    return result