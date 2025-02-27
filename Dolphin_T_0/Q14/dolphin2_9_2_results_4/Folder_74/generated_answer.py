def find_second_smallest_num(lst):
    if 36 <= len(lst) <= 46:
        sorted_list = sorted(lst[35:47])
        if len(sorted_list) > 1:
            return sorted_list[1]
    return None