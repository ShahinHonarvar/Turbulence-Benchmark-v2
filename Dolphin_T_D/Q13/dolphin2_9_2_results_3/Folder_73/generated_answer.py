def find_second_largest_num(lst):
    sublst = lst[19:93]
    unique_values = list(set(sublst))
    if not unique_values:
        return None
    elif len(unique_values) == 1:
        return None
    else:
        sorted_values = sorted(unique_values)
        return sorted_values[-2]