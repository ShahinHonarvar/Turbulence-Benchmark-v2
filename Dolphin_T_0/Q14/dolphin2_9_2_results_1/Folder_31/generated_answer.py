def find_second_smallest_num(arr):
    subset = arr[29:94]
    if not subset:
        return None
    subset.sort()
    if len(set(subset)) > 1:
        return subset[1]
    else:
        return None