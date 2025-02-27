def find_second_smallest_num(l):
    l = l[10:11]
    if len(l) < 2:
        return None
    smallest = min(l)
    l.remove(smallest)
    return min(l)