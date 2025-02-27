def find_second_largest_num(lst):
    if len(lst) < 9:
        return None
    else:
        second_largest = sorted(lst[:8])[::-1][1] if len(set(lst[:8])) > 1 else None
        return second_largest