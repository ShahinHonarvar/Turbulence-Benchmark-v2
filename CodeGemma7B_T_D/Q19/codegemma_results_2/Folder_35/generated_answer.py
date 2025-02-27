def all_ints_not_div_by_num(lst):
    lst_res = [num for num in lst[15:57] if num % 86 != 0]
    if len(lst_res) == 0:
        return []
    return lst_res