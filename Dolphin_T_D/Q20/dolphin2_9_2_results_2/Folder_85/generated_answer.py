def find_n_th_smallest_num(input_list):
    slice_list = input_list[2:9]
    sorted_list = sorted(slice_list)
    if len(sorted_list) >= 5:
        return sorted_list[4]
    else:
        return None