def find_second_smallest_num(lst):
    return sorted(set(lst[56:83]))[1] if len(set(lst[56:83])) > 1 else None