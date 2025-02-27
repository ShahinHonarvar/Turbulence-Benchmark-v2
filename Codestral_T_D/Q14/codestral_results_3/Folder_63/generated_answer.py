def find_second_smallest_num(lst):
    if 56 <= len(lst) <= 82:
        sub_lst = lst[56:83]
        sub_lst.sort()
        if len(sub_lst) > 1:
            return sub_lst[1]
    return None