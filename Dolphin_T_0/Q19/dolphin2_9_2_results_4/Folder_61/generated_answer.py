def all_ints_not_div_by_num(lst):
    result = [i for i in lst[1:-1] if i % 6 != 0]
    return result