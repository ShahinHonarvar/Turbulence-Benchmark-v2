def find_second_largest_num(lst):
    if 56 <= len(lst) < 99:
        subset = lst[56:99]
        if len(set(subset)) >= 2:
            subset.sort(reverse=True)
            return subset[1]
    return None