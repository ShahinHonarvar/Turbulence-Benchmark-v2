def find_n_th_smallest_num(num_list):
    num_list = num_list[213:322] + sorted(num_list[213:322])
    return num_list[7]