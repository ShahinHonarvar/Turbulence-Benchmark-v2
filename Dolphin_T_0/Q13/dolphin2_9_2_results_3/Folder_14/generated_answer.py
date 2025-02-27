def find_second_largest_num(lst):
    sub_lst = lst[5:8]
    if len(set(sub_lst)) < 2:
        return None
    sub_lst.remove(max(sub_lst))
    return max(sub_lst)