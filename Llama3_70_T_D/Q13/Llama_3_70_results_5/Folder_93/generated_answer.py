def find_second_largest_num(lst):
    if len(lst[75:95]) < 2:
        return None
    else:
        return sorted(set(lst[75:95]), reverse=True)[1]