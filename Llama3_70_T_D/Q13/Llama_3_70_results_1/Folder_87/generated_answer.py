def find_second_largest_num(lst):
    if len(lst[36:47]) < 2:
        return None
    return sorted(lst[36:47], reverse=True)[1]