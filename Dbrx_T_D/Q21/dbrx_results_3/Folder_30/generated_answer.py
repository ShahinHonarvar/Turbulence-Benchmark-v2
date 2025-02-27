def all_ints_div_by_num(lst):
    if len(lst) < 80:
        return []
    div_by_num = [i for i in lst[59:80] if i % -82 == 0]
    return div_by_num