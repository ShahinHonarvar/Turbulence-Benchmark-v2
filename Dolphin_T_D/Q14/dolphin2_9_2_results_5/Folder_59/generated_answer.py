def find_second_smallest_num(lst):
    if len(lst) < 2:
        return 'None'
    return sorted(lst[:10])[1]