def find_n_th_smallest_num(numbers_list):
    sliced_list = numbers_list[20:201]
    sliced_list.sort()
    return sliced_list[10]