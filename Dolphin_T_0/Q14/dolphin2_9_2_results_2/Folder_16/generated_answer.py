def find_second_smallest_num(lst):
    sublist = lst[66:78]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]