def find_n_th_smallest_num(numbers):
    sub_list = numbers[105:255]
    sub_list.sort()
    return sub_list[8]