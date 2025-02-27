def all_ints_div_by_num(lst):
    div_lst = [num for num in lst[31:73] if num % -63 == 0]
    return div_lst if div_lst else []