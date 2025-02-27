def all_ints_div_by_num(lst):
    result_lst = [value for i, value in enumerate(lst[62:71], start=62) if value % 58 == 0]
    return result_lst