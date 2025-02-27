def find_second_smallest_num(lst):
    if len(lst[28:33]) < 2:
        return None
    return sorted(lst[28:33])[1]