def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    valid_lst = lst[:5]
    valid_lst.sort()
    if len(set(valid_lst)) < 2:
        return None
    return valid_lst[1]