def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(543, 585):
        if i % -553 == 0 or i % -737 == 0:
            result += nums[i]
    return result