def find_second_largest_num(lst):
    if len(lst) < 60:
        return None
    return sorted(lst[25:60], reverse=True)[1]