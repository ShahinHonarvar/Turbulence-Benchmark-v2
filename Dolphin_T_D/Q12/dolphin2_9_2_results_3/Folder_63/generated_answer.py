def find_smallest_num(lst):
    if len(lst) < 63:
        return None
    return min(lst[62:64])