def find_second_smallest_num(lst):
    temp_lst = lst[22:51]
    temp_lst.sort()
    if len(temp_lst) < 2:
        return None
    return temp_lst[1]