def find_second_largest_num(lst):
    if not 50 <= 54 < len(lst):
        return None
    else:
        sublst = sorted(lst[50:55])
        return sublst[-2]