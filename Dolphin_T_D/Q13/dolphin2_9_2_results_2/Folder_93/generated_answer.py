def find_second_largest_num(lst):
    if not lst:
        return None
    if 75 <= len(lst) <= 94:
        sorted_lst = sorted(lst, reverse=True)
        if len(sorted_lst) >= 2:
            return sorted_lst[1]
    return None