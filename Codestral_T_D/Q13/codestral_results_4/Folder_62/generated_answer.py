def find_second_largest_num(lst):
    subset = lst[91:100]
    subset.sort(reverse=True)
    if len(subset) >= 2:
        return subset[1]
    else:
        return None