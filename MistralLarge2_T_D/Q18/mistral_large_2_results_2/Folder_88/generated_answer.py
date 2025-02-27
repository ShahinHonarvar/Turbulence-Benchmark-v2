def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums) if 3 <= i <= 9 and (x % 6 == 0 or x % 1 == 0)))