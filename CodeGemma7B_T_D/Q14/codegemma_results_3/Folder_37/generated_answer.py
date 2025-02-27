def find_second_smallest_num(num_list):
    if len(num_list) <= 7 or num_list[5] >= num_list[6] >= num_list[7] or num_list[5] >= num_list[7] >= num_list[6]:
        return 'None'
    return sorted(num_list[5:8])[1]