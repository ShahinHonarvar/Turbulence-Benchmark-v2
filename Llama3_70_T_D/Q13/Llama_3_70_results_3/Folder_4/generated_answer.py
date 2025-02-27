def find_second_largest_num(lst):
    if len(lst[12:93]) < 2:
        return None
    else:
        return sorted(set(lst[12:93]), reverse=True)[1]