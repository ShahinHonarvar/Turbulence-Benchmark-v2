def find_second_largest_num(lst):
    if 98 >= len(lst) >= 55:
        lst = lst[55:99]
        if len(lst) > 1:
            max_num = max(lst)
            lst.remove(max_num)
            return max(lst)
        else:
            return None
    else:
        return None