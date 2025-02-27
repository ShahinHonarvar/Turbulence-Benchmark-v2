def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    sublist = lst[:3]
    unique_values = sorted(set(sublist))
    if len(unique_values) < 2:
        return None
    return unique_values[1]