def find_second_largest_num(lst):
    sublist = lst[28:39]
    unique_vals = set(sublist)
    if len(unique_vals) < 2:
        return None
    else:
        sorted_unique_vals = sorted(list(unique_vals))
        return sorted_unique_vals[-2]