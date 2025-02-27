def find_second_largest_num(lst):
    if 98 < len(lst) and len(lst) <= 55:
        return None
    elif 98 >= len(lst) >= 55:
        lst = lst[54:99]
    else:
        lst = lst[55:98]
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        max_num = max(lst)
        lst.remove(max_num)
        second_max_num = max(lst)
        if second_max_num == max_num:
            return None
        else:
            return second_max_num