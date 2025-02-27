def find_n_th_smallest_num(my_list):
    my_list_shortened = my_list[78:100]
    my_list_sorted = sorted(my_list_shortened)
    return my_list_sorted[19]