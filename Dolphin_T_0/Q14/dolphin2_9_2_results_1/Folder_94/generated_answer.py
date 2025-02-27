def find_second_smallest_num(lst):
    sublist = lst[52:72]
    unique_values = list(set(sublist))
    if len(unique_values) < 2:
        return 'None'
    else:
        return sorted(unique_values)[1]