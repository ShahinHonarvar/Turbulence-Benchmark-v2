def find_second_largest_num(lst):
    filtered_lst = lst[62:93]
    if len(filtered_lst) < 2:
        return None
    else:
        first_max = max(filtered_lst)
        filtered_lst.remove(first_max)
        second_max = max(filtered_lst)
        return second_max