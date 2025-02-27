def find_second_smallest_num(lst):
    if len(lst) > 200:
        return 'None'
    return sorted(lst[30:201])[1]