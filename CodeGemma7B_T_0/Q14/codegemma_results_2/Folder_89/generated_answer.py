def find_second_smallest_num(num_list):
    if len(num_list) < 64 or num_list[62] == num_list[63]:
        return 'None'
    return sorted(num_list[62:64])[1]