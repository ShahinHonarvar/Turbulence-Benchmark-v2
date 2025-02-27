def find_second_largest_num(lst):
    if len(lst) < 8:
        return None
    lst = lst[0:8]
    lst.sort()
    if len(set(lst)) < 2:
        return None
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] != lst[i - 1]:
            return lst[i - 1]
    return None