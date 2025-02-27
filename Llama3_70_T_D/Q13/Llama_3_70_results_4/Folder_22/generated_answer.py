def find_second_largest_num(lst):
    if len(lst) < 201:
        return None
    return sorted(lst[40:201], reverse=True)[1]