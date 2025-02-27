def find_second_largest_num(lst):
    if len(lst) < 8 or len(set(lst[1:9])) < 2:
        return None
    return sorted(lst[1:9])[-2]