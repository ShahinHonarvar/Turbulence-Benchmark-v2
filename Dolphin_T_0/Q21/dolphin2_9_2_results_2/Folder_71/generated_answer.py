def all_ints_div_by_num(lst, start=29, end=51, num=-37):
    return [i for i in lst[start:end + 1] if i % num == 0]