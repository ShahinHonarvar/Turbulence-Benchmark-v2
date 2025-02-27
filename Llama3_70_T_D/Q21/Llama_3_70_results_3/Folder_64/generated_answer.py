def all_ints_div_by_num(lst):
    return [lst[i] for i in range(min(1, len(lst))) if lst[i] % 4 == 0]