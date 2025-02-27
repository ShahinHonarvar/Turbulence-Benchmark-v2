def find_second_largest_num(lst):
    if len(lst[4:]) < 2:
        return None
    return sorted(lst[4:], reverse=True)[1]