def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in nums[8:10]:
        if i % -3 == 0 or i % 6 == 0:
            result += i
    return result