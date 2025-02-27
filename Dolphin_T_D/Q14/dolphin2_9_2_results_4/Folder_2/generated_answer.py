def find_second_smallest_num(lst):
    if len(lst) < 87:
        return None
    part_lst = lst[43:87]
    part_lst.sort()
    if len(part_lst) < 2:
        return None
    return part_lst[1]