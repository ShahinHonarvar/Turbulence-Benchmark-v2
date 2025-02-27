def find_second_smallest_num(lst):
    if 37 <= len(lst) <= 76:
        return None
    else:
        subsection = lst[37:77]
        subsection.sort()
        return subsection[1]