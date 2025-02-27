def find_second_smallest_num(lst):
    if len(lst) < 85:
        return None
    else:
        sub_lst = lst[70:85]
        if len(set(sub_lst)) < 2:
            return None
        else:
            sub_lst.sort()
            return sub_lst[1]