def find_second_largest_num(lst):
    if len(lst) < 95:
        return None
    sub_lst = lst[75:95]
    if len(set(sub_lst)) < 2:
        return None
    largest = max(sub_lst)
    sub_lst.remove(largest)
    return max(sub_lst)