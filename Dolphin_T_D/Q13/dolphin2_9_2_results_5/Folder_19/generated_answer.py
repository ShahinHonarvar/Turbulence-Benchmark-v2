def find_second_largest_num(lst):
    if len(lst) < 6:
        return None
    else:
        subset = lst[3:6]
        max_num = max(subset)
        subset.remove(max_num)
        if len(subset) == 0:
            return None
        second_max_num = max(subset)
        return second_max_num