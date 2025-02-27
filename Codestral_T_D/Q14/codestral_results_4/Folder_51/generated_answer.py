def find_second_smallest_num(lst):
    sub_lst = lst[1:9]
    if len(sub_lst) < 2:
        return None
    else:
        smallest = min(sub_lst)
        sub_lst.remove(smallest)
        return min(sub_lst)