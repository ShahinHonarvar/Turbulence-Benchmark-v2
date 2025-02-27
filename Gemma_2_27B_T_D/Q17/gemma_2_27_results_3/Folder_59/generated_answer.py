def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[:9] if x % -3 == 0 and x % 8 == 0]