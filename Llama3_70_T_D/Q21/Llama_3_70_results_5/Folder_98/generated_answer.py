def all_ints_div_by_num(lst):
    return [lst[i] for i in range(len(lst)) if lst[i] % 6 == 0 and 0 <= i <= 0]