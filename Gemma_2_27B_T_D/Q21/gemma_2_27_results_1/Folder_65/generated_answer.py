def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i in range(14, 57) and num % -59 == 0]