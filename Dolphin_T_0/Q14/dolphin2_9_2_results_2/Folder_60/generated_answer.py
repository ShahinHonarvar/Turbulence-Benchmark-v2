def find_second_smallest_num(lst):
    if len(lst) > 98:
        subset = lst[56:99]
        subset.sort()
        return subset[1] if len(subset) > 1 else None
    else:
        return None