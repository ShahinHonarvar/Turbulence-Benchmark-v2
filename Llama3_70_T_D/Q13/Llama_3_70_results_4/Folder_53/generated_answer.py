def find_second_largest_num(lst):
    if len(lst) < 201:
        return None
    else:
        return sorted(set(lst[100:201]), reverse=True)[1] if len(set(lst[100:201])) > 1 else None