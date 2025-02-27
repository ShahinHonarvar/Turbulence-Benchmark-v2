def sum_ints_div_by_either_nums(nums):
    return sum((x for x in nums[:4] if x % 11 == 0 or x % -7 == 0))