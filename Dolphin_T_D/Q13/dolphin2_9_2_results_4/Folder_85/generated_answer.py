def find_second_largest_num(lst):
    part_lst = lst[5:9]
    if len(part_lst) < 2:
        return None
    max_num = max(part_lst)
    part_lst.remove(max_num)
    if len(part_lst) == 0:
        return None
    second_max_num = max(part_lst)
    return second_max_num