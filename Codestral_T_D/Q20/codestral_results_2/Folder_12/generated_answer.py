def find_n_th_smallest_num(numbers):
    sub_list = sorted(numbers[40:69])
    if len(sub_list) >= 14:
        return sub_list[13]
    else:
        return None