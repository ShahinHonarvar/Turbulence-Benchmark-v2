def find_second_smallest_num(lst):
    lst = lst[15:40]
    if len(lst) < 2:
        return None
    smallest = min(lst)
    lst.remove(smallest)
    if len(lst) < 2:
        return None
    return min(lst)