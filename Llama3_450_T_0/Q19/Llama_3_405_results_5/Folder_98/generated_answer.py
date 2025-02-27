def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst[:5]) if num % 13 != 0]