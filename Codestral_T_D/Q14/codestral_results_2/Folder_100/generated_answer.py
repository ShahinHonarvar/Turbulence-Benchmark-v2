def find_second_smallest_num(lst):
    if 43 > len(lst) - 1 or 51 > len(lst) - 1:
        return None
    sub_list = sorted(lst[43:52])
    return sub_list[1] if len(sub_list) > 1 else None