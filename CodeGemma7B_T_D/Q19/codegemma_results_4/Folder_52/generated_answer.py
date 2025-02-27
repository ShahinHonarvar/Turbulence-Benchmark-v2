def all_ints_not_div_by_num(lst):
    return [int for int in lst[50:92] if int % 16 != 0] or []