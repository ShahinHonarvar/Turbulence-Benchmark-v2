def find_second_smallest_num(lst):
    if len(lst) < 71:
        return None
    else:
        sub_lst = lst[51:72]
        if len(set(sub_lst)) < 2:
            return None
        else:
            sub_lst.sort()
            return sub_lst[1]