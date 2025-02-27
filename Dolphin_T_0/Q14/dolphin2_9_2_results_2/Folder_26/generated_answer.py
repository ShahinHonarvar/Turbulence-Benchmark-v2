def find_second_smallest_num(lst):
    if len(lst) < 2 or len(lst) < 78:
        return None
    else:
        subset = lst[62:79]
        min1 = min(subset)
        subset.remove(min1)
        if len(subset) < 2:
            return None
        else:
            min2 = min(subset)
            return min2