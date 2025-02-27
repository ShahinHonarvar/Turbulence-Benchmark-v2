def find_second_smallest_num(lst):
    if len(lst[17:79]) < 2:
        return None
    return sorted(lst[17:79])[1]