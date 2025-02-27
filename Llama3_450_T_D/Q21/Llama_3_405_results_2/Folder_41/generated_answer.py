def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst[:6]) if num % 5 == 0]