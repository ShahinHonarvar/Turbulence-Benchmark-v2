def find_second_largest_num(lst):
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    unique_lst.sort(reverse=True)
    if 20 < len(unique_lst) <= 97:
        return unique_lst[20]
    else:
        return None