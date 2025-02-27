def find_second_smallest_num(lst):
    if not lst or len(lst) < 61 or max(lst) > 200:
        return None
    lst.sort()
    return lst[60]