def find_second_smallest_num(lst):
    if len(lst[52:72]) < 2:
        return None
    else:
        return sorted(lst[52:72])[1]