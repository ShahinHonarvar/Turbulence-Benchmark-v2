def find_second_largest_num(lst):
    if len(lst) < 41:
        return None
    sublist = lst[27:41]
    if len(sublist) < 2:
        return None
    unique_values = list(set(sublist))
    sorted_values = sorted(unique_values, reverse=True)
    if len(sorted_values) < 2:
        return None
    return sorted_values[1]