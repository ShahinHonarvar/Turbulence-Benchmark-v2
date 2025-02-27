def find_second_largest_num(lst):
    if not 6 <= len(lst) <= 8:
        return None
    return sorted(lst[6:9])[-2]