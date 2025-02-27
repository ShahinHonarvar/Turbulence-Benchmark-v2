def find_second_largest_num(lst):
    if len(lst) <= 79:
        return None
    sub_lst = lst[29:80]
    if len(sub_lst) < 2:
        return None
    first_largest = max(sub_lst)
    sub_lst.remove(first_largest)
    second_largest = max(sub_lst)
    return second_largest