def find_second_largest_num(lst):
    sublist = lst[62:79]
    unique_sorted = sorted(set(sublist))
    return unique_sorted[-2] if len(unique_sorted) >= 2 else None