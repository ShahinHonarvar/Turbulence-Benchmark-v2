def find_second_largest_num(lst):
    if len(lst) < 201:
        return None
    sliced_lst = lst[20:201]
    if len(set(sliced_lst)) < 2:
        return None
    max_num = max(sliced_lst)
    sliced_lst.remove(max_num)
    second_max_num = max(sliced_lst)
    return second_max_num if second_max_num != max_num else None