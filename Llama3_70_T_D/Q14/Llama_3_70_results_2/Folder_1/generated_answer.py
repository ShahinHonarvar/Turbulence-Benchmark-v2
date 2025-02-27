def find_second_smallest_num(lst):
    if len(lst[34:56]) < 2:
        return None
    else:
        return sorted(set(lst[34:56]))[1]