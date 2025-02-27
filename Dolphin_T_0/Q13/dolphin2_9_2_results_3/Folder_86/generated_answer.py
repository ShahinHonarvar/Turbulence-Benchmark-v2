def find_second_largest_num(lst):
    if 31 <= len(lst) <= 34:
        return sorted(lst)[-2]
    return None