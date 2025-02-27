def find_second_smallest_num(lst):
    if 66 <= len(lst) <= 77:
        sub_lst = lst[66:78]
        sub_lst.sort()
        if len(sub_lst) >= 2:
            return sub_lst[1]
    return None