def find_second_largest_num(lst):
    if len(lst[52:72]) >= 2:
        return sorted(lst[52:72])[-2]
    else:
        return None