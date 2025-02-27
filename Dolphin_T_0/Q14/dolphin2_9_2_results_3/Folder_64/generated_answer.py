def find_second_smallest_num(lst):
    lst = lst[0:5]
    if not set(lst):
        return None
    if len(set(lst)) < 2:
        return None
    return sorted(lst)[1]