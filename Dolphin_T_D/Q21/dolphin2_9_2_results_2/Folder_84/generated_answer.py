def all_ints_div_by_num(lst):
    div_by_93 = [x for x in lst[52:54] if x % 93 == 0]
    return div_by_93 if div_by_93 else []