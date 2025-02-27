def find_second_smallest_num(lst):
    sliced_lst = lst[66:78]
    if len(sliced_lst) < 2:
        return None
    min_num = min(sliced_lst)
    sliced_lst.remove(min_num)
    return min(sliced_lst)