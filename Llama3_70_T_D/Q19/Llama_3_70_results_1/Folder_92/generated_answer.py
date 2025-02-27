def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if 0 < i < 1 and num % -1 != 0]