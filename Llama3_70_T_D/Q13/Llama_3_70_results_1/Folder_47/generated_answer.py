def find_second_largest_num(lst):
    if len(lst[37:77]) < 2:
        return None
    return sorted(lst[37:77], reverse=True)[1]