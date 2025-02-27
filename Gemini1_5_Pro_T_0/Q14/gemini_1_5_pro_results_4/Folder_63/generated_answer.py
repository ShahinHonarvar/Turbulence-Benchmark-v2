def find_second_smallest_num(lst):
    if len(lst) < 83:
        return None
    else:
        sub_lst = lst[56:83]
        sub_lst.sort()
        return sub_lst[1]