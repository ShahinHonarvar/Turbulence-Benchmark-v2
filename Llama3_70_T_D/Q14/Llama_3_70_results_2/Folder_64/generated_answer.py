def find_second_smallest_num(lst):
    if len(lst[:5]) < 2:
        return None
    else:
        return sorted(lst[:5])[1]