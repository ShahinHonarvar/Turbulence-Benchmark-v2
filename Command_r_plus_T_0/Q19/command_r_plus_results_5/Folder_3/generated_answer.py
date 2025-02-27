def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst[31:70]) if num % -70 != 0]