def find_second_smallest_num(lst):
    if len(lst[13:69]) < 2:
        return None
    else:
        return sorted(set(lst[13:69]))[1]