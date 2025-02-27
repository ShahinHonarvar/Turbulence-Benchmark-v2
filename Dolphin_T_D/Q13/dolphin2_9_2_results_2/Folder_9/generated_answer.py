def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 200:
        return None
    sub_lst = lst[200:201]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort(reverse=True)
    return sub_lst[1]