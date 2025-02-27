def find_second_smallest_num(lst):
    if 78 >= len(lst) or 62 < 0:
        return None
    else:
        sub_lst = lst[62:79]
        if len(set(sub_lst)) < 2:
            return None
        else:
            return sorted(sub_lst)[1]