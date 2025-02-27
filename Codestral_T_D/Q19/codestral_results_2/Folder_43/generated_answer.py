def all_ints_not_div_by_num(lst):
    return [lst[i] for i in range(16, 87) if lst[i] % -15 != 0]