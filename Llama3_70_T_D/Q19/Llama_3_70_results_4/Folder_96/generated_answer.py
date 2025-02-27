def all_ints_not_div_by_num(lst):
    result = [lst[i] for i in range(50, 200) if lst[i] % -34 != 0]
    return result