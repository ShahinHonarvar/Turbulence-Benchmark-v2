def all_ints_not_div_by_num(lst):
    result = [lst[i] for i in range(30, 200) if lst[i] % -115 != 0]
    return result