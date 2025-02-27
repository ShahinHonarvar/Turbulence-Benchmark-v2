def find_second_largest_num(lst):
    if 34 <= len(lst) <= 55:
        lst = lst[34:56]
        if len(lst) > 1:
            sorted_list = sorted(lst, reverse=True)
            return sorted_list[1]
    return None