def all_ints_div_by_num(lst):
    div_by_89 = [i for i in lst[16:63] if i % 89 == 0]
    return div_by_89 if len(div_by_89) > 0 else []