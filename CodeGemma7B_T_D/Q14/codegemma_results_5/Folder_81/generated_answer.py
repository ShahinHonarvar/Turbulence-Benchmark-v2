def find_second_smallest_num(lst):
    if not lst or len(lst) < 10:
        return 'None'
    sorted_lst = sorted(lst[10:100 + 1])
    return sorted_lst[1] if len(sorted_lst) > 1 else 'None'