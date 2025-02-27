def find_second_largest_num(lst):
    sub_list = sorted(lst[30:49], reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None