def find_second_smallest_num(lst):
    if len(lst) < 34:
        return None
    else:
        sub_lst = lst[31:35]
        sub_lst.sort()
        return sub_lst[1] if len(sub_lst) > 1 else None