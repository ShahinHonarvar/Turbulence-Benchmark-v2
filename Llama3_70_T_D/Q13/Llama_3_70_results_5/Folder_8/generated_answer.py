def find_second_largest_num(lst):
    if len(lst) <= 23:
        return None
    num_lst = lst[23:24]
    if len(num_lst) == 0:
        return None
    num_lst.sort(reverse=True)
    if len(num_lst) < 2:
        return None
    return num_lst[1]