def find_n_th_smallest_num(numbers):
    sub_list = numbers[15:32]
    sub_list.sort()
    if len(sub_list) >= 10:
        return sub_list[9]
    return None