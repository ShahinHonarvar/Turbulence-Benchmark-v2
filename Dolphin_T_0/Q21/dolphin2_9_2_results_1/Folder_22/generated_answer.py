def all_ints_div_by_num(lst):
    divisible_nums = [num for num in lst[10:11] if num % 1 == 0]
    return divisible_nums if len(divisible_nums) > 0 else []