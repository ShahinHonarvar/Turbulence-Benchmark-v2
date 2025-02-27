def all_ints_not_div_by_num(nums):
    return [x for i, x in enumerate(nums) if i > 766 and i < 905 and (x % -430 != 0)]