def find_second_largest_num(lst):
    if len(lst) <= 200:
        return None
    sublist = lst[40:201]
    return sorted(set(sublist), reverse=True)[1] if len(set(sublist)) > 1 else None