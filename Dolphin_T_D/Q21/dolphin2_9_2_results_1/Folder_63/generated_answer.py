def all_ints_div_by_num(lst, num=84, start=50, end=54):
    return [x for x in lst[start:end + 1] if x % num == 0]