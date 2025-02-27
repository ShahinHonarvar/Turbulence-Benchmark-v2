def find_second_smallest_num(lst):
    if 50 <= len(lst) <= 54:
        sorted_lst = sorted(lst[50:55])
        if len(sorted_lst) > 1:
            return sorted_lst[1]
    return None