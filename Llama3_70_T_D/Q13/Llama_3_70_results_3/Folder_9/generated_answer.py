def find_second_largest_num(lst):
    if len(lst) < 201:
        return None
    sublist = lst[200:201]
    if len(sublist) < 1:
        return None
    return max(sublist) if max(sublist) != min(sublist) else None