def find_second_largest_num(lst):
    lst = lst[43:87]
    if len(lst) > 1:
        max_num = max(lst)
        lst.remove(max_num)
        second_max_num = max(lst)
        return second_max_num
    else:
        return None