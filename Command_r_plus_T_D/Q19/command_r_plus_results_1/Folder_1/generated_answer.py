def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst[21:69], start=21) if num % -69 != 0]