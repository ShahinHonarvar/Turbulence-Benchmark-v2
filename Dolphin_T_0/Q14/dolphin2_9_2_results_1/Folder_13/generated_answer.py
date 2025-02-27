def find_second_smallest_num(lst):
    subset = lst[28:33]
    subset.sort()
    if len(subset) < 2:
        return None
    else:
        return subset[1]