def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    max_val = max(lst[:10])
    lst.remove(max_val)
    second_max = max(lst[:10])
    return second_max