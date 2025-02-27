def find_n_th_smallest_num(num_list):
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = (num_list[j], num_list[i])
    return num_list[12]