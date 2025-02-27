def find_second_largest_num(lst):
    if len(lst) < 69:
        return None
    else:
        return sorted(lst[42:69], reverse=True)[1] if len(set(lst[42:69])) > 1 else None