def all_ints_div_by_num(lst, start=14, end=68, num=18):
    return [x for x in lst[start:end + 1] if x % num == 0]