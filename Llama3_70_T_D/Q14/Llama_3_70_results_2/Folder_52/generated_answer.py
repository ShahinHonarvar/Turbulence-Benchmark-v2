def find_second_smallest_num(lst):
    if len(lst[64:67]) < 2:
        return None
    return sorted(lst[64:67])[1]