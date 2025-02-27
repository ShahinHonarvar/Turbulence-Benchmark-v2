def find_second_largest_num(lst):
    return sorted(lst[64:67], reverse=True)[1] if len(lst[64:67]) > 1 else None