def find_second_smallest_num(lst):
    if len(lst[56:99]) < 2:
        return None
    return sorted(lst[56:99])[1]