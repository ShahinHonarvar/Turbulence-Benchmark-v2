def find_second_smallest_num(lst):
    if len(lst) < 201:
        return None
    else:
        sliced_lst = lst[80:201]
        sorted_lst = sorted(sliced_lst)
        if len(sorted_lst) < 2:
            return None
        else:
            return sorted_lst[1]