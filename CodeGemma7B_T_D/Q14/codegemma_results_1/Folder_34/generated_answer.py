def find_second_smallest_num(lst):
    sorted_lst = sorted(lst[60:201])
    if len(sorted_lst) < 2:
        return 'None'
    return sorted_lst[1]