def sum_ints_div_by_either_nums(nums):
    return sum((i for i in nums[:10] if i % 6 == 0 or i % -3 == 0))