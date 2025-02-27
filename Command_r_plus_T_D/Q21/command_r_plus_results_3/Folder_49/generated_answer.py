def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst[30:301], 30) if num % 5 == 0]