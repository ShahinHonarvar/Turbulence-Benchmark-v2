def find_second_smallest_num(lst):
    if len(lst[30:35]) < 2:
        return None
    return sorted(lst[30:35])[1]