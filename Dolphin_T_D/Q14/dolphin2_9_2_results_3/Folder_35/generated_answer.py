def find_second_smallest_num(lst):
    if 15 <= len(lst) <= 39:
        sorted_lst = sorted(lst[15:40])
        if len(sorted_lst) > 1:
            return sorted_lst[1]
    return None