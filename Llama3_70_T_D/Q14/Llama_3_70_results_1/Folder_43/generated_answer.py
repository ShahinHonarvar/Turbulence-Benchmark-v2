def find_second_smallest_num(lst):
    if len(lst[74:96]) < 2:
        return None
    sub_lst = sorted(set(lst[74:96]))
    return sub_lst[1]