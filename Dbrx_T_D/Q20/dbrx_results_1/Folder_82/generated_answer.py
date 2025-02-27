def find_n_th_smallest_num(input_list):
    if len(input_list) < 15:
        return None
    else:
        sorted_list = sorted(input_list[:15])
        return sorted_list[14]