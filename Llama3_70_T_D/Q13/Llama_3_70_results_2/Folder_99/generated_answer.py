def find_second_largest_num(lst):
    if len(lst[310:371]) < 2:
        return None
    else:
        return sorted(set(lst[310:371]), reverse=True)[1]