def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    return sorted(lst[0:3])[1]