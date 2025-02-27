def find_second_largest_num(lst):
    if 19 <= len(lst) <= 92:
        part_lst = sorted(lst[19:93], reverse=True)
        if len(part_lst) > 1:
            return part_lst[1]
    return None