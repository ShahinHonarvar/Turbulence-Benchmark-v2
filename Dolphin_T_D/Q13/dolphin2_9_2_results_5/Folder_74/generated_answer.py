def find_second_largest_num(lst):
    sub_lst = lst[16:79]
    sub_lst.sort(reverse=True)
    if len(sub_lst) < 2:
        return None
    else:
        return sub_lst[1]