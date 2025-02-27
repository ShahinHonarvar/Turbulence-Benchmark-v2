def find_second_largest_num(l):
    if len(l) < 43 or len(l) > 51:
        return None
    sorted_list = sorted(l[43:52], reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]