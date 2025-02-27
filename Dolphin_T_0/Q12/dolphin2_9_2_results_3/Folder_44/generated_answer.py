def find_smallest_num(lst):
    if len(lst) <= 66:
        return min(lst[10:66])
    else:
        return None