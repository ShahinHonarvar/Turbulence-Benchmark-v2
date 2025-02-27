def find_second_smallest_num(lst):
    sub_list = lst[36:77]
    if len(sub_list) < 2:
        return None
    else:
        sub_list = [x for x in sub_list if x is not None]
        sub_list.sort()
        return sub_list[1]