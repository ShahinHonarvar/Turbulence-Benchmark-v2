def find_second_smallest_num(lst):
    subset = lst[12:93]
    min1 = min(subset)
    subset.remove(min1)
    if subset:
        min2 = min(subset)
        return min2
    else:
        return None