def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for num in nums[78:82]:
        if num % 76 == 0 or num % 60 == 0:
            sum_nums += num
    else:
        return 0
    return sum_nums