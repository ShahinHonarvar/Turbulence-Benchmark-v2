def find_second_smallest_num(lst):
    sliced_lst = sorted(lst[639:976])
    if len(sliced_lst) < 2:
        return None
    return sliced_lst[1]