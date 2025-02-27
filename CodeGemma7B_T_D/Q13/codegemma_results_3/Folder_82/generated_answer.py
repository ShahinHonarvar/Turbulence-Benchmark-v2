def find_second_largest_num(lst):
    if len(lst) < 20 or (idx := lst.index(20)) > (idx := lst.index(200)):
        return None
    if idx == len(lst) - 1:
        return lst[idx - 1]
    return lst[idx + 1]