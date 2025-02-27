def find_second_smallest_num(lst):
    if len(lst) < 55:
        return None
    subsection_list = lst[34:56]
    if len(set(subsection_list)) < 2:
        return None
    subsection_list.sort()
    return subsection_list[1]