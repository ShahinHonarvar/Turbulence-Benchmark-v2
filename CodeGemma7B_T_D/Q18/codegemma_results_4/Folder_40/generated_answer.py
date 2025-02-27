def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[0:2 + 1]:
        if num % 2 == 0 or num % 1 == 0:
            result += num
    return result