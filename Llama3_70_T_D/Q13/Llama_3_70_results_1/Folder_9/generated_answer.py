def find_second_largest_num(lst):
    return sorted(lst[200:201])[1] if len(lst[200:201]) > 1 else None