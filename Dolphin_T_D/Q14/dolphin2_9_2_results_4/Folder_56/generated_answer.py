def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    smallest = min(lst)
    lst.remove(smallest)
    if len(lst) == 1:
        return None
    second_smallest = min(lst)
    return second_smallest