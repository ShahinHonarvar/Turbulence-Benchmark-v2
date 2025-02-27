def find_second_smallest_num(lst):
    subset = lst[62:79]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]