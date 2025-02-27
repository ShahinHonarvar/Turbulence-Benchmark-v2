def find_second_smallest_num(lst):
    if len(lst) < 40 or len(lst[15:40]) < 2:
        return None
    sub_list = sorted(lst[15:40])
    return sub_list[1]