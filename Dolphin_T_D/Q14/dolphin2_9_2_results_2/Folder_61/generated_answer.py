def find_second_smallest_num(lst):
    if len(lst) < 8:
        return None
    smallest = min(lst[:8])
    lst.remove(smallest)
    if lst:
        return min(lst[:8])
    else:
        return None