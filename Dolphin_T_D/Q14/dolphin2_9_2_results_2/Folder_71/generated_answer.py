def find_second_smallest_num(lst):
    part_lst = lst[29:52]
    if len(part_lst) < 2:
        return None
    else:
        return sorted(part_lst)[1]