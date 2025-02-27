def find_second_smallest_num(lst):
    if len(lst) < 201 or 50 >= len(lst):
        return None
    sliced_lst = lst[50:201]
    sorted_lst = sorted(sliced_lst)
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]