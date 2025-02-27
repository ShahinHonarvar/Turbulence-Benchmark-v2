def all_ints_not_div_by_num(lst):
    return [int for int in lst[50:81] if int % 64 != 0]