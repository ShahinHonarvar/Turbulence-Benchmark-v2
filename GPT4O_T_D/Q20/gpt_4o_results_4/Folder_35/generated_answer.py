def find_n_th_smallest_num(numbers):
    sub_list = numbers[12:61]
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[5] if len(sorted_sub_list) >= 6 else None