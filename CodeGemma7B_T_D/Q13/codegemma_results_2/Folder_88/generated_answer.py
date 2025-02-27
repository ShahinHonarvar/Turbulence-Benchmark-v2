def find_second_largest_num(lst):
    lst = lst[4:9]
    lst.sort(reverse=True)
    if len(lst) < 2:
        return None
    return lst[1]