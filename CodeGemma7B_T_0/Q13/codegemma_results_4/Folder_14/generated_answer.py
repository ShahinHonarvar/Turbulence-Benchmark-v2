def find_second_largest_num(num_list):
    if len(num_list) < 8 or num_list[5] == num_list[6] == num_list[7]:
        return 'None'
    return sorted(num_list[5:8])[-2]