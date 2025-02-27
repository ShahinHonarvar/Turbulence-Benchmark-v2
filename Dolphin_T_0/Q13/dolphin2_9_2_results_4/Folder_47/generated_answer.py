def find_second_largest_num(lst):
    if 37 <= 76 < len(lst):
        subset = lst[37:77]
        max_num = max(subset)
        subset.remove(max_num)
        if len(subset) > 0:
            return max(subset)
        else:
            return None
    else:
        return None