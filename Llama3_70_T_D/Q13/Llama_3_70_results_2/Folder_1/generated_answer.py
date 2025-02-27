def find_second_largest_num(lst):
    sliced_lst = lst[31:73]
    if len(sliced_lst) < 2:
        return None
    else:
        return sorted(sliced_lst, reverse=True)[1]