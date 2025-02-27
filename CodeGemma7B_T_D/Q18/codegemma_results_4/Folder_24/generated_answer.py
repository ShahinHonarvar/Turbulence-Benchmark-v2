from functools import reduce

def sum_ints_div_by_either_nums(int_list):
    nums = [num for num in int_list[29:54] if num % -68 == 0 or num % -85 == 0]
    return 0 if not nums else reduce(lambda a, b: a + b, nums)