def sum_ints_div_by_either_nums(nums):
    return sum((i for i in nums[:3] if i % -2 == 0 or i % 3 == 0))