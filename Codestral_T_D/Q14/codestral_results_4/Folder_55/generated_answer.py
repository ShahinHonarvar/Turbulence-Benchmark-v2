def find_second_smallest_num(lst):
    if 10 < len(lst):
        sorted_list = sorted(lst[10:11])
        if len(sorted_list) > 1:
            return sorted_list[1]
    return None