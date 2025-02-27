def find_second_smallest_num(lst):
    if not lst or len(lst) < 3:
        return 'None'
    sorted_lst = sorted(lst[25:88])
    if len(sorted_lst) <= 1:
        return 'None'
    return sorted_lst[1]