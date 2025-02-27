def find_second_largest_num(lst):
    if len(lst) < 80 or len(lst) > 29:
        return None
    sliced_lst = lst[29:80]
    if len(set(sliced_lst)) < 2:
        return None
    else:
        return sorted(set(sliced_lst), reverse=True)[1]