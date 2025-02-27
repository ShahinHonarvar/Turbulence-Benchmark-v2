def all_ints_not_div_by_num(int_list):
    if 81 < len(int_list) < 86:
        return [i for i in int_list[81:86] if i % 77 != 0]
    elif len(int_list) >= 86:
        return [i for i in int_list[81:86] if i % 77 != 0] or []
    else:
        return []