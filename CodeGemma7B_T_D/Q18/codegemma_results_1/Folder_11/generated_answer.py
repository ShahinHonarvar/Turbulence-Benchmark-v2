def sum_ints_div_by_either_nums(nums):
    sum = 0
    for x in nums[22:25]:
        if (x % 85 == 0 or x % 30) == 0:
            sum += x
    return sum