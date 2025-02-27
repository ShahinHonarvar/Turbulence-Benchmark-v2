def find_n_th_smallest_num(numbers):
    sub_list = numbers[20:201]
    sub_list.sort()
    return sub_list[10]