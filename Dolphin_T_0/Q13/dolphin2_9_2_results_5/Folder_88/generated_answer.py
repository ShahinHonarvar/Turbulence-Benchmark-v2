def find_second_largest_num(lst):
    subset = lst[4:9]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]