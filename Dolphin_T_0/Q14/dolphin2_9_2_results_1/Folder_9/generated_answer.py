def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    subsection = lst[200:70:-1]
    if len(subsection) < 2:
        return None
    subsection.sort()
    for num in subsection[1:]:
        if num != subsection[0]:
            return num
    return None