def all_ints_not_div_by_num(lst):
    return [lst[i] for i in range(1, len(lst) - 1) if lst[i] % 8 != 0]