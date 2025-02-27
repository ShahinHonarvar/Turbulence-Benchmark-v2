def find_n_th_smallest_num(numbers):
    sub_list = numbers[10:101]
    sub_list.sort()
    return sub_list[9]