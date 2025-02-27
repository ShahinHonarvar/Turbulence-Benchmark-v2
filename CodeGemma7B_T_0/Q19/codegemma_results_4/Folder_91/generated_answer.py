def all_ints_not_div_by_num(nums):
    return [num for num in nums if num % 8 != 0 and num in range(0, 4)]