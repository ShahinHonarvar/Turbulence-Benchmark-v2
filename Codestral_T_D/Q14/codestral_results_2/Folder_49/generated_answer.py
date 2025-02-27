def find_second_smallest_num(lst):
    sub_lst = lst[80:201]
    if len(sub_lst) < 2:
        return None
    else:
        sub_lst.sort()
        return sub_lst[1]