def find_second_largest_num(lst):
    if len(lst) < 9:
        return None
    return sorted(lst[:9], reverse=True)[1]