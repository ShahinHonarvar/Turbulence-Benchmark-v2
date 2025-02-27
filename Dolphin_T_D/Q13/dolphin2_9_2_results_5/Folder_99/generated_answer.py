def find_second_largest_num(lst):
    subsection = lst[310:371]
    if len(subsection) < 2:
        return None
    else:
        subsection.sort()
        return subsection[-2]