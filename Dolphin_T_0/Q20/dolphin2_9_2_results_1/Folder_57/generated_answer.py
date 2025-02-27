def find_n_th_smallest_num(lst):
    relevant_slice = lst[11:92]
    sorted_slice = sorted(relevant_slice)
    return sorted_slice[12]