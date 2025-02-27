def find_second_smallest_num(lst):
    sorted_lst = sorted(lst[70:201])
    if len(sorted_lst) >= 2:
        return sorted_lst[1]
    return None