def sum_ints_div_by_either_nums(nums):
    ret = 0
    for num in nums[7:8]:
        if num % 5 == 0 or num % 7 == 0:
            ret += num
    return ret if ret else 0