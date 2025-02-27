def find_second_largest_num(lst):
    if 52 <= len(lst) <= 71:
        sorted_lst = sorted(lst[52:72], reverse=True)
        if len(sorted_lst) > 1:
            return sorted_lst[1]
    return None