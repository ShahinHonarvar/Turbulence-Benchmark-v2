def find_second_largest_num(lst):
    subset = lst[3:5]
    if len(subset) < 2:
        return None
    else:
        subset_sorted = sorted(set(subset), reverse=True)
        return subset_sorted[1]