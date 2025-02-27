def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    lst.sort(reverse=True)
    if lst[8] != lst[9]:
        return lst[9]
    return None