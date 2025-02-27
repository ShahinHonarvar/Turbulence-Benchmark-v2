def find_second_smallest_num(lst):
    if 66 <= len(lst) <= 93:
        sorted_lst = sorted(lst[66:94])
        if len(sorted_lst) > 1:
            return sorted_lst[1]
    return None