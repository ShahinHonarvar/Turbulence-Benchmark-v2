def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if 2 < i < 7 and num % 8 != 0]