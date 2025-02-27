def find_second_largest_num(lst):
    if 29 < len(lst) <= 79:
        slice_list = lst[29:80]
        unique_values = list(set(slice_list))
        unique_values.sort(reverse=True)
        if len(unique_values) > 1:
            return unique_values[1]
    return None