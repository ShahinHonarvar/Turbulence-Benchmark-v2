def find_second_smallest_num(lst):
    if not lst or len(lst) < 81:
        return None
    sorted_lst = sorted(lst[91:100])
    return sorted_lst[1] if len(sorted_lst) > 1 else None