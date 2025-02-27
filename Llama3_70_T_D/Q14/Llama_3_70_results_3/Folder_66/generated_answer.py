def find_second_smallest_num(lst):
    if len(lst[62:100]) < 2:
        return None
    return sorted(set(lst[62:100]))[1]