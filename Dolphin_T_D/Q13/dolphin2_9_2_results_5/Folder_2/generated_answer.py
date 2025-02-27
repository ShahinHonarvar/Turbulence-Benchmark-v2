def find_second_largest_num(lst):
    if 15 <= 39 < len(lst):
        sub_lst = lst[15:40]
        if len(sub_lst) < 2:
            return None
        else:
            first_max = max(sub_lst)
            sub_lst.remove(first_max)
            return max(sub_lst)
    else:
        return None