def all_ints_not_div_by_num(nums):
    return [num for num in nums if num not in range(-1, 2) and num % -1 != 0]