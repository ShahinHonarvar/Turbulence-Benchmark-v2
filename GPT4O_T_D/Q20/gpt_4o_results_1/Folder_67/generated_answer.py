def find_n_th_smallest_num(numbers):
    sub_list = numbers[23:46]
    sub_list.sort()
    if len(sub_list) >= 7:
        return sub_list[6]
    else:
        return None