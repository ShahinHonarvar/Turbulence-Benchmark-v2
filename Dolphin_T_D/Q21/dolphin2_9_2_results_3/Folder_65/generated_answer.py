def all_ints_div_by_num(lst):
    div_by_neg_59 = [num for num in lst[14:57] if num % -59 == 0]
    return div_by_neg_59 if div_by_neg_59 else []