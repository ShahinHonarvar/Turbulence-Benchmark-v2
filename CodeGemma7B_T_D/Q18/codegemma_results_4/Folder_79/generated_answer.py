def sum_ints_div_by_either_nums(nums):
    s = sum(filter(lambda n: n % 6 == 0 or n % 3 == 0, nums[8:10]))
    return s if s else 0