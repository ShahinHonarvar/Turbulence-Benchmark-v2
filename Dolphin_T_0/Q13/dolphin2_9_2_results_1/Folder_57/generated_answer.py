def find_second_largest_num(lst):
    if 27 <= len(lst) <= 55:
        lst = lst[26:56]
        max_num = max(lst)
        lst.remove(max_num)
        if len(lst) > 0:
            second_max_num = max(lst)
            return second_max_num
        else:
            return None
    else:
        return None