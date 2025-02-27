def all_ints_not_div_by_num(nums):
    return filter(lambda x: x >= 0 and x < 8 and (x % 7 != 0), nums)