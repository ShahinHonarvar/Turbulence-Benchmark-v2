def find_second_smallest_num(l):
    sub_list = l[310:371]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    elif len(set(sub_list)) < 2:
        return None
    else:
        return sub_list[1]