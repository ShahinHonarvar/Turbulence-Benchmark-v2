def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[46:92]:
        if num % 67 == 0 or num % 15 == 0:
            result += num
    return result