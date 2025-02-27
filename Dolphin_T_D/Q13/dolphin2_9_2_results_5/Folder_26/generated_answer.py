def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 99:
        return None
    sliced_lst = lst[62:100]
    if len(sliced_lst) < 2:
        return None
    first = max(sliced_lst)
    sliced_lst.remove(first)
    second = max(sliced_lst)
    return second