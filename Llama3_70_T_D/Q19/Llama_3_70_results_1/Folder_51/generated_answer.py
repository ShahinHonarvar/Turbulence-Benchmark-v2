def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if 1 < i < 6 and num % 2 != 0]