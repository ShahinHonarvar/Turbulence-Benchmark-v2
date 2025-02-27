def find_second_smallest_num(lst):
    if 66 <= 77 < len(lst):
        sub_list = sorted(lst[66:78])
        if len(sub_list) > 1:
            return sub_list[1]
    return None