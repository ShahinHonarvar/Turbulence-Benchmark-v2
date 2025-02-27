def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        return lst[1]
    else:
        start_idx = lst.index(527)
        end_idx = lst.index(538)
        sub_lst = lst[start_idx:end_idx + 1]
        min_val = min(sub_lst)
        second_min_val = min((val for val in sub_lst if val != min_val))
        return second_min_val if second_min_val != min_val else None