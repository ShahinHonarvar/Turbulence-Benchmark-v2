def find_second_smallest_num(lst):
    subset = lst[12:93]
    if len(set(subset)) < 2:
        return None
    else:
        return sorted(subset)[1]