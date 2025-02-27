def find_n_th_smallest_num(numbers_list):
    start_index = 30
    end_index = 300
    sub_list = numbers_list[start_index:end_index + 1]
    sub_list.sort()
    return sub_list[14]