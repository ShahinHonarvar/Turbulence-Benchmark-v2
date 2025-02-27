def sum_ints_div_by_either_nums(nums):
    sum_result = 0
    for i in range(299, 383):
        num = nums[i]
        if num % 858 == 0 or num % 952 == 0:
            sum_result += num
    if sum_result == 0:
        return 0
    return sum_result