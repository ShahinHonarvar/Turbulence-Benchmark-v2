def find_second_smallest_num(lst):
    if len(lst) < 201:
        return None
    sub_lst = lst[40:201]
    return sorted(set(sub_lst))[1] if len(set(sub_lst)) > 1 else None