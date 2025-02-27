def find_n_th_smallest_num(lst):
    selected_range = lst[20:63]
    selected_range.sort()
    return selected_range[11]