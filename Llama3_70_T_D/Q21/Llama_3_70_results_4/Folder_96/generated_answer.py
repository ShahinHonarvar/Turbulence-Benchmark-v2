def all_ints_div_by_num(lst):
    return [lst[i] for i in range(min(max(20, 0), len(lst)), min(max(20, 0), len(lst)) + 1) if lst[i] % 2 == 0]