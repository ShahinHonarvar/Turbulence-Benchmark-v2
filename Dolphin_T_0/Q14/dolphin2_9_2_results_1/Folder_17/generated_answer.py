def find_second_smallest_num(lst):
    section = lst[28:39]
    if len(section) < 2:
        return None
    else:
        section.sort()
        return section[1]