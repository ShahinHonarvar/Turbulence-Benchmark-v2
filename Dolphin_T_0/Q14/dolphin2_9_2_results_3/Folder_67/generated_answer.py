def find_second_smallest_num(lst):
    sub_lst = lst[50:55]
    if len(set(sub_lst)) < 2:
        return None
    return sorted(sub_lst)[1]