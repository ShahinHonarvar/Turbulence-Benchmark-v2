def find_second_largest_num(lst):
    if len(lst) < 200:
        return None
    else:
        section = lst[40:201]
        if len(set(section)) < 2:
            return None
        else:
            section.sort()
            return section[-2]